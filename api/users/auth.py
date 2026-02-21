from collections.abc import Callable
from datetime import UTC, datetime, timedelta
from functools import wraps
from typing import Any

import jwt
from flask import Response, g, jsonify, request

from api.constants import SECRET_KEY, TOKEN_EXPIRY_DAYS
from api.models.user import User


def token_from_request() -> str | None:
    token = None
    if "Authorization" in request.headers:
        auth_header = request.headers["Authorization"]
        if auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]

    return token


def create_token(user_id: int) -> str:
    payload = {
        "user_id": user_id,
        "exp": datetime.now(UTC) + timedelta(days=TOKEN_EXPIRY_DAYS),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


def decode_token(token: str) -> dict[str, Any] | None:
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


def permission_denied() -> Response:
    return jsonify({})  # TODO: implemente correct "Permission denied" response


def login_required(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)  # retains function name and metadata
    def decorated_function(*args, **kwargs):
        token = token_from_request()
        if not token:
            return permission_denied()
        payload = decode_token(token)
        if not payload:
            return permission_denied()
        g.current_user = User.get_by_id(payload["user_id"])
        return func(*args, **kwargs)

    return decorated_function


def is_logged_in() -> bool:
    return g.current_user is not None


def admin_required(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)  # retains function name and metadata
    def decorated_function(*args, **kwargs):
        if not is_logged_in():
            return permission_denied()
        if not g.current_user.is_admin():
            return permission_denied()
        return func(*args, **kwargs)

    return decorated_function
