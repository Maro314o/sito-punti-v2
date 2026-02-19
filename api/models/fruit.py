from api.database import db
import datetime


class Fruit(db.Model):
    """
    Fruit model representing a fruit-related event.

    Attributes:
        id (int): Primary key
        date (datetime): Date and time of the fruit event
        event_type (str): Type of fruit event
        season (int): Season number the event belongs to
        quantity (int): Quantity of fruit
        user_id (int): Foreign key to the user table

    Relationships:
        user (relationship): Many-to-one relationship with User model
    """

    id: int = db.Column(db.Integer, primary_key=True)
    date: datetime.datetime = db.Column(db.DateTime, nullable=False)
    event_type: str = db.Column(db.String(150))
    season: int = db.Column(db.Integer)
    quantity: int = db.Column(db.Integer)
    user_id: int = db.Column(db.Integer, db.ForeignKey("user.id"))

    @classmethod
    def get_by_id(cls, fruit_id: int) -> "Fruit":
        """
        Retrieve a fruit event by its ID.

        Args:
            fruit_id (int): The unique identifier of the fruit event.

        Returns:
            Fruit: The fruit event object with the specified ID.

        Raises:
            NoResultFound: If no fruit event with the given ID exists.
        """
        return cls.query.filter_by(id=fruit_id).one()

    @classmethod
    def get_by_user(cls, user_id: int) -> list["Fruit"]:
        """
        Retrieve all fruit events for a specific user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            list[Fruit]: List of all fruit events for the user.
        """
        return cls.query.filter_by(user_id=user_id).all()

