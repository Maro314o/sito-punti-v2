import datetime

from api.database import db


class Fruit(db.Model):
    """
    Fruit model representing a fruit-related event.

    Attributes:
        id (int): Primary key
        date (datetime): Date and time of the fruit event
        event_type (str): Type of fruit event
        season_id (int): Foreign key to the season table
        quantity (int): Quantity of fruit
        user_id (int): Foreign key to the user table
    """

    id: int = db.Column(db.Integer, primary_key=True)
    date: datetime.datetime = db.Column(db.DateTime, nullable=False)
    event_type: str = db.Column(db.String(150))
    season_id: int = db.Column(db.Integer, db.ForeignKey("season.id"))
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
