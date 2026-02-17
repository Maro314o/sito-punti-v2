import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv

from api.models import Utente, Classe, Squadra, Cronologia
from api.auth import auth_bp

from flask_sqlalchemy import SQLAlchemy
from .constants import DOTENV_FILE

load_dotenv(DOTENV_FILE)
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv(
        "SECRET_KEY", "dev-secret-key-change-in-production"
    )

    db_path = os.environ.get(
        "DB_PATH", os.path.join(os.path.dirname(__file__), "..", "data")
    )
    os.makedirs(db_path, exist_ok=True)
    db_file = os.path.join(db_path, "database.db")
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_file}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    cors_origins = os.environ.get(
        "CORS_ORIGINS",
        "http://localhost:3000,http://127.0.0.1:3000,http://localhost:3001",
    )
    CORS(
        app,
        supports_credentials=True,
        origins=cors_origins.split(","),
    )

    app.register_blueprint(auth_bp)

    with app.app_context():
        db.create_all()

        if not Classe.get_by_nome("admin"):
            db.session.add(Classe(nome_classe="admin", massimo_studenti_squadra=0))
            db.session.commit()

        if not Squadra.get_by_nome("admin"):
            admin_classe = Classe.get_by_nome("admin")
            if admin_classe:
                db.session.add(
                    Squadra(
                        nome_squadra="admin",
                        numero_componenti=0,
                        classe_id=admin_classe.id,
                    )
                )
                db.session.commit()

    @app.route("/api/health")
    def health():
        return jsonify({"status": "healthy", "service": "flask-api"})

    @app.route("/api/classes")
    def get_classes():
        classes = Classe.get_all_student_classes()
        return jsonify([c.to_dict() for c in classes])

    @app.route("/api/classes/<int:class_id>")
    def get_class(class_id):
        classe = Classe.get_by_id(class_id)
        if not classe:
            return jsonify({"error": "Class not found"}), 404
        return jsonify(classe.to_dict())

    @app.route("/api/classes/<int:class_id>/squadre")
    def get_squadre_by_class(class_id):
        squadre = Squadra.get_by_classe(class_id)
        return jsonify([s.to_dict() for s in squadre])

    @app.route("/api/squadre")
    def get_squadre():
        squadre = Squadra.get_all()
        return jsonify([s.to_dict() for s in squadre])

    @app.route("/api/squadre/<int:squadra_id>")
    def get_squadra(squadra_id):
        squadra = Squadra.get_by_id(squadra_id)
        if not squadra:
            return jsonify({"error": "Squadra not found"}), 404
        return jsonify(squadra.to_dict())

    @app.route("/api/students")
    def get_students():
        students = Utente.get_active_students()
        return jsonify([s.to_dict() for s in students])

    @app.route("/api/students/<int:student_id>")
    def get_student(student_id):
        student = Utente.get_by_id(student_id)
        if not student:
            return jsonify({"error": "Student not found"}), 404
        return jsonify(student.to_dict())

    @app.route("/api/students/<int:student_id>/points", methods=["GET"])
    def get_student_points(student_id):
        student = Utente.get_by_id(student_id)
        if not student:
            return jsonify({"error": "Student not found"}), 404

        stagione = request.args.get("stagione", type=int)
        if not stagione:
            return jsonify({"error": "Stagione parameter required"}), 400

        cronologia = Cronologia.get_by_utente_stagione(student_id, stagione)
        total_points = sum(c.modifica_punti for c in cronologia)

        return jsonify(
            {
                "student_id": student_id,
                "stagione": stagione,
                "total_points": total_points,
                "history": [c.to_dict() for c in cronologia],
            }
        )

    @app.route("/api/squadre/<int:squadra_id>/points", methods=["GET"])
    def get_squadra_points(squadra_id):
        squadra = Squadra.get_by_id(squadra_id)
        if not squadra:
            return jsonify({"error": "Squadra not found"}), 404

        stagione = request.args.get("stagione", type=int)
        if not stagione:
            return jsonify({"error": "Stagione parameter required"}), 400

        points = squadra.punti_stagione(stagione)

        return jsonify(
            {
                "squadra_id": squadra_id,
                "squadra_name": squadra.nome_squadra,
                "stagione": stagione,
                "points": points,
            }
        )

    @app.route("/api/test")
    def test_endpoint():
        return jsonify({"status": "success", "message": "Flask API is working!"})

    return app


app = create_app()
