from flask import Blueprint, jsonify, request

from api.models import User, SchoolClass, Team, Event

api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.route("/health")
def health():
    return jsonify({"status": "healthy", "service": "flask-api"})


@api_bp.route("/classes")
def get_classes():
    classes = SchoolClass.get_all_student_classes()
    return jsonify([c.to_dict() for c in classes])


@api_bp.route("/classes/<int:class_id>")
def get_class(class_id):
    classe = SchoolClass.get_by_id(class_id)
    if not classe:
        return jsonify({"error": "Class not found"}), 404
    return jsonify(classe.to_dict())


@api_bp.route("/classes/<int:class_id>/squadre")
def get_squadre_by_class(class_id):
    squadre = Team.get_by_class(class_id)
    return jsonify([s.to_dict() for s in squadre])


@api_bp.route("/squadre")
def get_squadre():
    squadre = Team.query.all()
    return jsonify([s.to_dict() for s in squadre])


@api_bp.route("/squadre/<int:squadra_id>")
def get_squadra(squadra_id):
    squadra = Team.get_by_id(squadra_id)
    if not squadra:
        return jsonify({"error": "Squadra not found"}), 404
    return jsonify(squadra.to_dict())


@api_bp.route("/students")
def get_students():
    students = User.get_active_students()
    return jsonify([s.to_dict() for s in students])


@api_bp.route("/students/<int:student_id>")
def get_student(student_id):
    student = User.get_by_id(student_id)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    return jsonify(student.to_dict())


@api_bp.route("/students/<int:student_id>/points", methods=["GET"])
def get_student_points(student_id):
    student = User.get_by_id(student_id)
    if not student:
        return jsonify({"error": "Student not found"}), 404

    stagione = request.args.get("stagione", type=int)
    if not stagione:
        return jsonify({"error": "Stagione parameter required"}), 400

    events = Event.query.filter_by(user_id=student_id, season_id=stagione).all()
    total_points = sum(e.points for e in events)

    return jsonify(
        {
            "student_id": student_id,
            "stagione": stagione,
            "total_points": total_points,
            "history": [e.to_dict() for e in events],
        }
    )


@api_bp.route("/squadre/<int:squadra_id>/points", methods=["GET"])
def get_squadra_points(squadra_id):
    squadra = Team.get_by_id(squadra_id)
    if not squadra:
        return jsonify({"error": "Squadra not found"}), 404

    stagione = request.args.get("stagione", type=int)
    if not stagione:
        return jsonify({"error": "Stagione parameter required"}), 400

    events = Event.query.filter_by(season_id=stagione).all()
    team_members = User.query.filter_by(team_id=squadra_id).all()
    team_member_ids = [m.id for m in team_members]
    team_events = [e for e in events if e.user_id in team_member_ids]
    points = sum(e.points for e in team_events)

    return jsonify(
        {
            "squadra_id": squadra_id,
            "squadra_name": squadra.name,
            "stagione": stagione,
            "points": points,
        }
    )


@api_bp.route("/test")
def test_endpoint():
    return jsonify({"status": "success", "message": "Flask API is working!"})
