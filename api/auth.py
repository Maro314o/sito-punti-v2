from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
import jwt
import os
from datetime import datetime, timedelta
from api.database import db
from api.models import Utente, Classe

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-change-in-production")
TOKEN_EXPIRY_DAYS = 7


def create_token(user_id, email, nominativo, admin_user):
    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(days=TOKEN_EXPIRY_DAYS),
        "iat": datetime.utcnow(),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


def decode_token(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    user = Utente.get_by_email(email)

    if not user:
        return jsonify({"error": "Invalid credentials"}), 401

    if not user.account_attivo:
        return jsonify({"error": "Account is not active"}), 401

    if not user.password:
        return jsonify({"error": "No password set for this account"}), 401

    if check_password_hash(user.password, password):
        token = create_token(user.id, user.email, user.nominativo, user.admin_user)
        return jsonify(
            {
                "success": True,
                "token": token,
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "nominativo": user.nominativo,
                    "admin": user.admin_user == 1,
                    "account_attivo": user.account_attivo == 1,
                },
            }
        )

    return jsonify({"error": "Invalid credentials"}), 401


@auth_bp.route("/logout", methods=["POST"])
def logout():
    return jsonify({"success": True, "message": "Logged out successfully"})


def token_required(f):
    def decorated(*args, **kwargs):
        token = None

        if "Authorization" in request.headers:
            auth_header = request.headers["Authorization"]
            if auth_header.startswith("Bearer "):
                token = auth_header.split(" ")[1]

        if not token:
            return jsonify({"error": "Token is missing"}), 401

        payload = decode_token(token)
        if not payload:
            return jsonify({"error": "Token is invalid or expired"}), 401

        request.user = payload
        return f(*args, **kwargs)

    return decorated


@auth_bp.route("/me", methods=["GET"])
@token_required
def get_current_user():
    return jsonify(request.user)


@auth_bp.route("/check", methods=["GET"])
def check_auth():
    token = None

    if "Authorization" in request.headers:
        auth_header = request.headers["Authorization"]
        if auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]

    if not token:
        return jsonify({"authenticated": False})

    payload = decode_token(token)
    if payload:
        return jsonify(
            {
                "authenticated": True,
                "user": {
                    "id": payload["user_id"],
                    "email": payload["email"],
                    "nominativo": payload["nominativo"],
                    "admin": payload["admin"],
                },
            }
        )
    return jsonify({"authenticated": False})


@auth_bp.route("/seed-admin", methods=["POST"])
def seed_admin():
    """Create a test admin user for testing"""
    data = request.get_json() or {}
    password = data.get("password", "admin123")

    existing_admin = Utente.get_by_email("admin@test.com")
    if existing_admin:
        return jsonify(
            {"message": "Admin already exists", "user": existing_admin.to_dict()}
        )

    admin_classe = Classe.get_by_nome("admin")
    if not admin_classe:
        admin_classe = Classe(nome_classe="admin", massimo_studenti_squadra=0)
        db.session.add(admin_classe)
        db.session.commit()

    hashed_password = generate_password_hash(password, method="pbkdf2:sha256")
    new_admin = Utente(
        email="admin@test.com",
        nominativo="Admin Test",
        password=hashed_password,
        admin_user=1,
        account_attivo=1,
        classe_id=admin_classe.id,
    )
    db.session.add(new_admin)
    db.session.commit()

    return jsonify(
        {
            "success": True,
            "message": "Admin user created",
            "user": new_admin.to_dict(),
            "password": password,
        }
    )
