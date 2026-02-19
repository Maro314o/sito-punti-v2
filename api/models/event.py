from api.database import db
import datetime


class Event(db.Model):
    """
    Event model representing a point-yielding event for a student.

    Attributes:
        id (int): Primary key
        date (datetime): Date and time of the event
        event_type (str): Type of event (e.g., "verifica", "bug", "motivational")
        event_variation (str): Variation of the event (e.g., "written", "oral")
        season (int): Season number the event belongs to
        points (float): Points awarded or deducted for this event
        user_id (int): Foreign key to the user table

    Relationships:
        user (relationship): Many-to-one relationship with User model
    """

    id: int = db.Column(db.Integer, primary_key=True)
    date: datetime.datetime = db.Column(db.DateTime, nullable=False)
    event_type: str = db.Column(db.String(150))
    event_variation: str = db.Column(db.String(150), nullable=True)
    season: int = db.Column(db.Integer)
    points: float = db.Column(db.Float)
    user_id: int = db.Column(db.Integer, db.ForeignKey("user.id"))

    @classmethod
    def get_by_id(cls, event_id: int) -> "Event":
        """
        Retrieve an event by its ID.

        Args:
            event_id (int): The unique identifier of the event.

        Returns:
            Event: The event object with the specified ID.

        Raises:
            NoResultFound: If no event with the given ID exists.
        """
        return cls.query.filter_by(id=event_id).one()

    @classmethod
    def get_by_user(cls, user_id: int) -> list["Event"]:
        """
        Retrieve all events for a specific user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            list[Event]: List of all events for the user.
        """
        return cls.query.filter_by(user_id=user_id).all()

