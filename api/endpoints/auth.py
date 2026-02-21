from flask import Blueprint, Response, jsonify, request
from werkzeug.security import check_password_hash

from api.api_models.request_models import LoginRequest
from api.api_models.response_models import ErrorResponse, TokenResponse
from api.models import User
from api.users.auth import create_token

auth = Blueprint("auth", __name__, url_prefix="/api/auth")


@auth.route("/generate_token", methods=["POST"])
def generate_token() -> tuple[Response, int]:
    try:
        data = LoginRequest(**request.get_json())
    except Exception:
        error = ErrorResponse(error="Invalid request body")
        return jsonify(error.model_dump()), 400

    user = User.exists_by_email(data.email)
    if not user:
        error = ErrorResponse(error="Invalid credentials")
        return jsonify(error.model_dump()), 401

    if not user.active_account:
        error = ErrorResponse(error="Account is not active")
        return jsonify(error.model_dump()), 401

    if check_password_hash(user.password, data.password):
        token = create_token(user.id, user.email, user.nominativo, user.admin_user)
        response = TokenResponse(token=token)
        return jsonify(response.model_dump()), 200

    error = ErrorResponse(error="Invalid credentials")
    return jsonify(error.model_dump()), 401


@auth.route("/check_token", methods=["POST"])
def check_token() -> tuple[Response, int]:
    data = request.get_json()
    if not data or "token" not in data:
        return jsonify({"valid": False}), 401

    from api.users.auth import decode_token

    payload = decode_token(data["token"])
    return jsonify({"valid": payload is not None}), 200
