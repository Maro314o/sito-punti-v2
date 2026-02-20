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
        season_id (int): Foreign key to the season table
        points (float): Points awarded or deducted for this event
        user_id (int): Foreign key to the user table
    """

    id: int = db.Column(db.Integer, primary_key=True)
    date: datetime.datetime = db.Column(db.DateTime, nullable=False)
    event_type: str = db.Column(db.String(150))
    event_variation: str = db.Column(db.String(150), nullable=True)
    season_id: int = db.Column(db.Integer, db.ForeignKey("season.id"))
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
