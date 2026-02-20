#!/usr/bin/env python3
import os
import sys
import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from api.database import db
from api.models import User, SchoolClass, Team, Event, Season, Year


def create_mock_db(db_path: str = "data/mock_database.db"):
    from flask import Flask

    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    if os.path.exists(db_path):
        os.remove(db_path)

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()

        admin_class = SchoolClass(class_name="admin", max_students_per_team=0)
        db.session.add(admin_class)
        db.session.commit()

        year = Year(
            school_grade=1,
            name="2025-2026",
            start=datetime.datetime(2025, 9, 1),
            end=datetime.datetime(2026, 6, 30),
        )
        db.session.add(year)
        db.session.commit()

        class_1 = SchoolClass(class_name="1A", max_students_per_team=4, year_id=year.id)
        class_2 = SchoolClass(class_name="1B", max_students_per_team=4, year_id=year.id)
        db.session.add(class_1)
        db.session.add(class_2)
        db.session.commit()

        admin_team = Team(name="admin", size=0, school_class_id=admin_class.id)
        db.session.add(admin_team)
        db.session.commit()

        team_1 = Team(name="Team Alpha", size=3, school_class_id=class_1.id)
        team_2 = Team(name="Team Beta", size=4, school_class_id=class_1.id)
        team_3 = Team(name="Team Gamma", size=2, school_class_id=class_2.id)
        db.session.add(team_1)
        db.session.add(team_2)
        db.session.add(team_3)
        db.session.commit()

        season_1 = Season(
            start=datetime.datetime(2025, 9, 1),
            end=datetime.datetime(2025, 12, 31),
            name="Autumn",
            season_number=1,
            class_id=class_1.id,
            year_id=year.id,
        )
        season_2 = Season(
            start=datetime.datetime(2026, 1, 1),
            end=datetime.datetime(2026, 6, 30),
            name="Spring",
            season_number=2,
            class_id=class_1.id,
            year_id=year.id,
        )
        db.session.add(season_1)
        db.session.add(season_2)
        db.session.commit()

        user1 = User(
            email="student1@test.com",
            full_name="Mario Rossi",
            team_name="Team Alpha",
            password="hashed_password",
            admin_user=0,
            active_account=1,
            school_class_id=class_1.id,
            team_id=team_1.id,
        )
        user2 = User(
            email="student2@test.com",
            full_name="Luca Bianchi",
            team_name="Team Beta",
            password="hashed_password",
            admin_user=0,
            active_account=1,
            school_class_id=class_1.id,
            team_id=team_2.id,
        )
        user3 = User(
            email="student3@test.com",
            full_name="Giulia Verdi",
            team_name="Team Gamma",
            password="hashed_password",
            admin_user=0,
            active_account=1,
            school_class_id=class_2.id,
            team_id=team_3.id,
        )
        admin = User(
            email="admin@test.com",
            full_name="Admin User",
            team_name="admin",
            password="hashed_password",
            admin_user=1,
            active_account=1,
            school_class_id=admin_class.id,
            team_id=admin_team.id,
        )
        db.session.add(user1)
        db.session.add(user2)
        db.session.add(user3)
        db.session.add(admin)
        db.session.commit()

        event1 = Event(
            date=datetime.datetime(2025, 10, 15),
            event_type="verifica",
            event_variation="written",
            season_id=season_1.id,
            points=8.5,
            user_id=user1.id,
        )
        event2 = Event(
            date=datetime.datetime(2025, 11, 20),
            event_type="interrogation",
            event_variation="oral",
            season_id=season_1.id,
            points=7.0,
            user_id=user1.id,
        )
        event3 = Event(
            date=datetime.datetime(2025, 12, 1),
            event_type="bug",
            event_variation="fixed",
            season_id=season_1.id,
            points=2.0,
            user_id=user2.id,
        )
        db.session.add(event1)
        db.session.add(event2)
        db.session.add(event3)
        db.session.commit()

        print(f"Mock database created at: {db_path}")
        print(f"  - {SchoolClass.query.count()} classes")
        print(f"  - {Team.query.count()} teams")
        print(f"  - {User.query.count()} users")
        print(f"  - {Season.query.count()} seasons")
        print(f"  - {Event.query.count()} events")


if __name__ == "__main__":
    db_path = sys.argv[1] if len(sys.argv) > 1 else "data/mock_database.db"
    create_mock_db(db_path)
