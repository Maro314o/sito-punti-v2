from api.database import db
import datetime


class Year(db.Model):
    """
    Year model representing a school year.

    Attributes:
        id (int): Primary key
        school_grade (int): Grade level of the year (unique)
        name (str): Name of the school year
        start (datetime): Start date and time of the year
        end (datetime): End date and time of the year

    Relationships:
        seasons (relationship): One-to-many relationship with Season model
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
    def get_by_grade(cls, school_grade: int) -> "Year | None":
        """
        Retrieve a year by its school grade level.

        Args:
            school_grade (int): The school grade level.

        Returns:
            Year | None: The year object if found, None otherwise.
        """
        return cls.query.filter_by(school_grade=school_grade).first()

    @classmethod
    def get_current(cls) -> "Year | None":
        """
        Retrieve the current active year based on current date.

        Returns:
            Year | None: The current year if found, None otherwise.
        """
        now = datetime.datetime.now()
        return cls.query.filter(cls.start <= now, cls.end >= now).first()
