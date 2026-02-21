import sys
from pathlib import Path

import pytest
from flask import Flask
from flask_cors import CORS

sys.path.insert(0, str(Path(__file__).parent.parent))

from api.database import db
from api.endpoints.auth import auth
from api.endpoints.routes import api_bp


@pytest.fixture
def app():
    test_app = Flask(__name__)
    test_app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    test_app.config["TESTING"] = True
    test_app.config["SECRET_KEY"] = "test-secret"

    db.init_app(test_app)
    CORS(test_app)
    test_app.register_blueprint(auth)
    test_app.register_blueprint(api_bp)

    with test_app.app_context():
        db.create_all()

        from api.models import SchoolClass, Team, User

        admin_class = SchoolClass(class_name="admin", max_students_per_team=0)
        db.session.add(admin_class)
        db.session.commit()

        team = Team(name="admin", size=0, school_class_id=admin_class.id)
        db.session.add(team)
        db.session.commit()

        admin = User(
            email="admin@test.com",
            full_name="Admin User",
            password="hashed_password",
            admin_user=1,
            active_account=1,
            school_class_id=admin_class.id,
            team_id=team.id,
        )
        db.session.add(admin)
        db.session.commit()

        yield test_app

        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


class TestHealthEndpoint:
    def test_health_check(self, client):
        response = client.get("/api/health")
        assert response.status_code == 200
        data = response.get_json()
        assert data["status"] == "healthy"
        assert data["service"] == "flask-api"


class TestClassesEndpoint:
    def test_get_classes_empty(self, client):
        response = client.get("/api/classes")
        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, list)

    def test_get_class_not_found(self, client):
        response = client.get("/api/classes/999")
        assert response.status_code == 404


class TestTeamsEndpoint:
    def test_get_teams_empty(self, client):
        response = client.get("/api/squadre")
        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, list)

    def test_get_team_not_found(self, client):
        response = client.get("/api/squadre/999")
        assert response.status_code == 404


class TestStudentsEndpoint:
    def test_get_students_empty(self, client):
        response = client.get("/api/students")
        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, list)

    def test_get_student_not_found(self, client):
        response = client.get("/api/students/999")
        assert response.status_code == 404


class TestPointsEndpoint:
    def test_get_student_points_missing_param(self, client):
        response = client.get("/api/students/1/points")
        assert response.status_code == 400

    def test_get_team_points_missing_param(self, client):
        response = client.get("/api/squadre/1/points")
        assert response.status_code == 400


class TestTestEndpoint:
    def test_test_endpoint(self, client):
        response = client.get("/api/test")
        assert response.status_code == 200
        data = response.get_json()
        assert data["status"] == "success"
        assert "Flask API is working!" in data["message"]
