import datetime

from api.database import db
from api.models import Season


class Year(db.Model):
    """
    Year model representing a school year.

    Attributes:
        id (int): Primary key
        school_grade (int): Grade level of the year (unique)
        name (str): Name of the school year
        start (datetime): Start date and time of the year
        end (datetime): End date and time of the year
    """

    id: int = db.Column(db.Integer, primary_key=True)
    school_grade: int = db.Column(db.Integer, unique=True)
    name: str = db.Column(db.String(150))
    start: datetime.datetime = db.Column(db.DateTime, nullable=False)
    end: datetime.datetime = db.Column(db.DateTime, nullable=False)
    seasons = db.relationship("Season", lazy="dynamic", backref="year")

    @classmethod
    def get_by_id(cls, year_id: int) -> "Year":
        """
        Retrieve a year by its ID.

        Args:
            year_id (int): The unique identifier of the year.

        Returns:
            Year: The year object with the specified ID.

        Raises:
            NoResultFound: If no year with the given ID exists.
        """
        return cls.query.filter_by(id=year_id).one()

    @classmethod
    def get_by_grade(cls, grade: int) -> "Year":
        return cls.query.filter_by(school_grade=grade).one()

    def get_season_of_class(self, class_id: int) -> list[Season]:
        return self.seasons.filter_by(class_id=class_id).all()
