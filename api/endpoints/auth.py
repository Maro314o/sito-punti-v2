from flask import Blueprint, jsonify, request
from werkzeug.security import check_password_hash, generate_password_hash

from api.database import db
from api.models import Classe, Utente
from api.users.auth import create_token

auth = Blueprint("auth", __name__, url_prefix="/api/auth")


@auth.route("/generate_token", methods=["POST"])
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


@auth_bp.route("/me", methods=["GET"])
@token_required
def get_current_user():
    return jsonify(request.user)
