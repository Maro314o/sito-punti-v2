from flask_login import UserMixin
from sqlalchemy import func
import datetime
from api.database import db


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
    team_name: str = db.Column(db.String(150), nullable=False)
    password: str = db.Column(db.String(150), nullable=False)
    admin_user: int = db.Column(db.Integer, default=0)
    active_account: int = db.Column(db.Integer, default=0)
    last_password_change: datetime.datetime = db.Column(
        db.DateTime, default=datetime.datetime.now
    )

    school_class_id: int = db.Column(db.Integer, db.ForeignKey("school_class.id"))
    team_id: int = db.Column(db.Integer, db.ForeignKey("team.id"))
    events= db.relationship("Event", lazy="dynamic", backref="user")

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
    def get_by_id(cls, user_id: int) -> "User":
        """
        Retrieve a user by their ID.

        Args:
            user_id (int): The unique identifier of the user.

        Returns:
            User: The user object with the specified ID.

        Raises:
            NoResultFound: If no user with the given ID exists.
        """
        return cls.query.filter_by(id=user_id).one()

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

    def to_dict(self) -> dict:
        """
        Convert the user object to a dictionary representation.

        Returns:
            dict: Dictionary containing user data with keys:
                - id (int): User's ID
                - email (str): User's email
                - full_name (str): User's full name
                - team_name (str): Team name
                - admin_user (int): Admin flag
                - active_account (int): Active account flag
                - school_class_id (int): Class ID
                - team_id (int): Team ID
        """
        return {
            "id": self.id,
            "email": self.email,
            "full_name": self.full_name,
            "team_name": self.team_name,
            "admin_user": self.admin_user,
            "active_account": self.active_account,
            "school_class_id": self.school_class_id,
            "team_id": self.team_id,
        }
