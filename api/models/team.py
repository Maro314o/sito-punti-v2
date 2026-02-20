from sqlalchemy import func

from api.database import db
from api.models.event import Event


class Team(db.Model):
    """
    Team model representing a team in the system.

    Attributes:
        id (int): Primary key
        name (str): Name of the team (unique)
        size (int): Number of members in the team
        school_class_id (int): Foreign key to the school_class table

    Relationships:
        members (relationship): One-to-many relationship with User model
        school_class (relationship): Many-to-one relationship with SchoolClass model
    """

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(150), unique=True)
    size: int = db.Column(db.Integer)

    school_class_id: int = db.Column(db.Integer, db.ForeignKey("school_class.id"))

    members = db.relationship("User", lazy="dynamic", backref="team")

    @classmethod
    def get_by_id(cls, team_id: int) -> "Team | None":
        """
        Retrieve a team by its ID.

        Args:
            team_id (int): The unique identifier of the team.

        Returns:
            Team | None: The team object if found, None otherwise.
        """
        return cls.query.filter_by(id=team_id).first()

    @classmethod
    def get_by_name(cls, team_name: str) -> "Team | None":
        """
        Retrieve a team by its name.

        Args:
            team_name (str): The name of the team.

        Returns:
            Team | None: The team object if found, None otherwise.
        """
        return cls.query.filter_by(name=team_name).first()

    @classmethod
    def get_by_class(cls, school_class_id: int) -> list["Team"]:
        """
        Retrieve all teams belonging to a specific class.

        Args:
            school_class_id (int): The ID of the school class.

        Returns:
            list[Team]: List of teams in the specified class.
        """
        return cls.query.filter_by(school_class_id=school_class_id).all()

    def get_points_of_season(self, season_id: int) -> float:
        """
        Get total points for the team in a specific season.

        Args:
            season_id: The ID of the season.

        Returns:
            float: Total points of all team members in the season.
        """
        result = (
            db.session.query(func.sum(Event.points))
            .join(self.members.property)
            .filter(Event.season_id == season_id)
            .scalar()
        )
        return result if result is not None else 0.0
