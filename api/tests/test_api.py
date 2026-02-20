import os
import sys
import pytest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from api.main import create_app
from api.database import db


@pytest.fixture
def app():
    test_db_path = "data/test_database.db"
    os.makedirs("data", exist_ok=True)

    if os.path.exists(test_db_path):
        os.remove(test_db_path)

    app = create_app()
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{test_db_path}"
    app.config["TESTING"] = True

    with app.app_context():
        db.create_all()

        from api.models import User, SchoolClass, Team

        admin_class = SchoolClass(class_name="admin", max_students_per_team=0)
        db.session.add(admin_class)
        db.session.commit()

        team = Team(name="admin", size=0, school_class_id=admin_class.id)
        db.session.add(team)
        db.session.commit()

        admin = User(
            email="admin@test.com",
            full_name="Admin User",
            team_name="admin",
            password="hashed_password",
            admin_user=1,
            active_account=1,
            school_class_id=admin_class.id,
            team_id=team.id,
        )
        db.session.add(admin)
        db.session.commit()

        yield app

        db.session.remove()
        db.drop_all()
        if os.path.exists(test_db_path):
            os.remove(test_db_path)


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
