import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

from api.auth import auth
from api.models import SchoolClass, Team, User
from api.routes import api_bp
from api.users.creation import construct_admin_user
from api.utils import require_env_var

from .constants import DATA_DIRECTORY, DATABASE_FILE, DOTENV_FILE, SECRET_KEY
from .database import db

load_dotenv(DOTENV_FILE)


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY

    os.makedirs(DATA_DIRECTORY, exist_ok=True)
    database_url = os.getenv("DATABASE_URL", f"sqlite:///{DATABASE_FILE}")
    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    #
    cors_origins = os.getenv(
        "CORS_ORIGINS",
        "http://localhost:3000,http://127.0.0.1:3000,http://localhost:3001",
    )  # cross origin,not needed if public api
    CORS(
        app,
        supports_credentials=True,
        origins=cors_origins.split(","),
    )
    #

    app.register_blueprint(auth)
    app.register_blueprint(api_bp)

    with app.app_context():
        db.create_all()

        if not SchoolClass.get_by_name("admin"):
            db.session.add(SchoolClass(class_name="admin", max_students_per_team=0))
            db.session.commit()

        if not Team.get_by_name("admin"):
            admin_class = SchoolClass.get_by_name("admin")
            if admin_class:
                db.session.add(
                    Team(
                        name="admin",
                        size=0,
                        school_class_id=admin_class.id,
                    )
                )
                db.session.commit()

        if not User.query.filter_by(email="s-admin.starter@isiskeynes.it").first():
            admin_user = construct_admin_user(
                email="s-admin.starter@isiskeynes.it",
                full_name="admin_starter",
                password=require_env_var("DEFAULT_ADMIN_PASSWORD"),
            )
            db.session.add(admin_user)
            db.session.commit()

    return app


app = create_app()
