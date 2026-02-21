import datetime

from flask_login import UserMixin
from sqlalchemy import func
from sqlalchemy.orm import Query

from api.database import db
from api.models.season import SchoolClass, Season
from api.models.team import Team


class User(db.Model, UserMixin):
    """
    User model representing a student or admin in the system.

    Attributes:
        id (int): Primary key
        email (str): User's email (unique)
        full_name (str): User's full name (unique)
        team_name (str): Team name the user belongs to
        password (str): User's password (hashed)
        admin_user (int): 1 if admin, 0 otherwise
        active_account (int): 1 if account is active, 0 otherwise
        last_password_change (datetime): Timestamp of last password change
        school_class_id (int): Foreign key to school_class table
        team_id (int): Foreign key to team table

    Relationships:
        team (relationship): Many-to-one relationship with Team model
        school_class (relationship): Many-to-one relationship with SchoolClass model
    """

    id: int = db.Column(db.Integer, primary_key=True)
    email: str = db.Column(db.String(150), unique=True)
    full_name: str = db.Column(db.String(150), unique=True)
    password: str = db.Column(db.String(150), nullable=False)
    admin_user: bool = db.Column(db.Boolean, default=0)
    active_account: bool = db.Column(db.Boolean, default=0)
    last_password_change: datetime.datetime = db.Column(db.DateTime, default=datetime.datetime.now)

    school_class_id: int = db.Column(db.Integer, db.ForeignKey("school_class.id"))
    team_id: int = db.Column(db.Integer, db.ForeignKey("team.id"))
    events = db.relationship("Event", lazy="dynamic", backref="user")

    def is_admin(self) -> bool:
        """
        Check if the user has admin privileges.

        Returns:
            bool: True if user is an admin, False otherwise.
        """
        return self.admin_user == 1

    def is_active_account(self) -> bool:
        """
        Check if the user's account is active.

        Returns:
            bool: True if account is active, False otherwise.
        """
        return self.active_account == 1

    @classmethod
    def get_by_id(cls, user_id: int) -> "User | None":
        """
        Retrieve a user by their ID.

        Args:
            user_id (int): The unique identifier of the user.

        Returns:
            User | None: The user object if found, None otherwise.
        """
        return cls.query.filter_by(id=user_id).first()

    @classmethod
    def get_by_full_name(cls, full_name: str) -> "User":
        """
        Retrieve a user by their full name.

        Args:
            full_name (str): The full name of the user.

        Returns:
            User: The user object with the specified full name.

        Raises:
            NoResultFound: If no user with the given full name exists.
        """
        return cls.query.filter_by(full_name=full_name).one()

    @classmethod
    def get_by_email(cls, email: str) -> "User":
        """
        Retrieve a user by their email address.

        Args:
            email (str): The email address of the user.

        Returns:
            User: The user object with the specified email.

        Raises:
            NoResultFound: If no user with the given email exists.
        """
        return cls.query.filter_by(email=email).one()

    @classmethod
    def exists_by_email(cls, email: str) -> "User | None":
        """Check if a user with the given email exists."""
        return cls.query.filter_by(email=email).first()

    @classmethod
    def exists_by_full_name(cls, full_name: str) -> "User | None":
        """Check if a user with the given full name exists."""
        return cls.query.filter_by(full_name=full_name).first()

    @classmethod
    def get_all_students(cls) -> list["User"]:
        """
        Retrieve all users who are students (non-admin users).

        Returns:
            list[User]: List of all student users.
        """
        return cls.query.filter_by(admin_user=0).all()

    @classmethod
    def get_all_admins(cls) -> list["User"]:
        """
        Retrieve all users who are administrators.

        Returns:
            list[User]: List of all admin users.
        """
        return cls.query.filter_by(admin_user=1).all()

    @classmethod
    def get_active_students(cls) -> list["User"]:
        """
        Retrieve all students with active accounts.

        Returns:
            list[User]: List of all active student users.
        """
        return cls.query.filter_by(admin_user=0, active_account=1).all()

    def get_points_of_season(self, season: Season | int) -> float:
        season_id: int = -1
        if type(season) is int:
            season_id = Season.get_by_number_and_class_id(season, self.school_class_id).id
        elif type(season) is Season:
            season_id = season.id

        season_events: Query = self.events.query.filter_by(season_id=season_id)
        column_sum_query: Query = season_events.with_entities(func.sum(self.events.points))
        total_points_of_season = column_sum_query.scalar()

        return total_points_of_season

    def core_info(self):
        return {
            "id": self.id,
            "email": self.email,
            "full_name": self.full_name,
            "school_class_name": SchoolClass.get_by_id(self.school_class_id).name,
            "team_id": Team.get_by_id(self.team_id).name,
        }

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "full_name": self.full_name,
            "admin_user": self.admin_user,
            "active_account": self.active_account,
            "school_class_id": self.school_class_id,
            "team_id": self.team_id,
        }
