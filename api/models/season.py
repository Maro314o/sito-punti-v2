from api.database import db
import datetime


class Season(db.Model):
    """
    Season model representing a season within a school year.

    Attributes:
        id (int): Primary key
        start (datetime): Start date and time of the season
        end (datetime): End date and time of the season
        name (str): Name of the season (e.g., "Autumn", "Spring")
        season_number (int): Sequential number of the season within the year
        class_id (int): Foreign key to the school_class table
        year_id (int): Foreign key to the year table
    """

    id: int = db.Column(db.Integer, primary_key=True)
    start: datetime.datetime = db.Column(db.DateTime, nullable=False)
    end: datetime.datetime = db.Column(db.DateTime, nullable=False)
    name: str = db.Column(db.String(150))
    season_number: int = db.Column(db.Integer)
    class_id: int = db.Column(db.Integer, db.ForeignKey("school_class.id"))
    year_id: int = db.Column(db.Integer, db.ForeignKey("year.id"))

    @classmethod
    def get_by_id(cls, season_id: int) -> "Season":
        """
        Retrieve a season by its ID.

        Args:
            season_id (int): The unique identifier of the season.

        Returns:
            Season: The season object with the specified ID.

        Raises:
            NoResultFound: If no season with the given ID exists.
        """
        return cls.query.filter_by(id=season_id).one()

    @classmethod
    def get_by_number_and_class_id(cls, number: int, class_id: int) -> "Season":
        return cls.query.filter_by(number=number, class_id=class_id).one()
