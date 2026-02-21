from flask import Blueprint, g, jsonify, request

from api.models import Event, SchoolClass, Team, User
from api.utils import login_required

api = Blueprint("api", __name__, url_prefix="/api")


@api.route("/me", methods=["GET"])
@login_required
def get_current_user():
    return jsonify(g.get_current_user.core_info())


@api.route("/health")
def health():
    return jsonify({"status": "healthy", "service": "sito-punti-python-api"})




