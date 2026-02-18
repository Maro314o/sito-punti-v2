from api.database import db


class SchoolClass(db.Model):
    """
    SchoolClass model representing a class in the system.

    Attributes:
        id (int): Primary key
        class_name (str): Name of the class (unique)
        max_students_per_team (int): Maximum number of students per team

    Relationships:
        teams (relationship): One-to-many relationship with Team model
        students (relationship): One-to-many relationship with User model
    """

    id: int = db.Column(db.Integer, primary_key=True)
    class_name: str = db.Column(db.String(150), unique=True)
    max_students_per_team: int = db.Column(db.Integer)

    teams = db.relationship("Team", lazy="dynamic", backref="school_class")
    students = db.relationship("User", lazy="dynamic", backref="school_class")

    @classmethod
    def get_by_id(cls, class_id: int) -> "SchoolClass | None":
        """
        Retrieve a class by its ID.

        Args:
            class_id (int): The unique identifier of the class.

        Returns:
            SchoolClass | None: The class object if found, None otherwise.
        """
        return cls.query.filter_by(id=class_id).first()

    @classmethod
    def get_by_name(cls, class_name: str) -> "SchoolClass | None":
        """
        Retrieve a class by its name.

        Args:
            class_name (str): The name of the class.

        Returns:
            SchoolClass | None: The class object if found, None otherwise.
        """
        return cls.query.filter_by(class_name=class_name).first()

    @classmethod
    def get_all(cls) -> list["SchoolClass"]:
        """
        Retrieve all classes.

        Returns:
            list[SchoolClass]: List of all classes.
        """
        return cls.query.all()

    @classmethod
    def get_all_student_classes(cls) -> list["SchoolClass"]:
        """
        Retrieve all classes that are available for students (excludes admin and no-team).

        Returns:
            list[SchoolClass]: List of all student-available classes.
        """
        not_available = ["admin", "Nessuna_squadra"]
        return cls.query.filter(~cls.class_name.in_(not_available)).all()

    def to_dict(self) -> dict:
        """
        Convert the class object to a dictionary representation.

        Returns:
            dict: Dictionary containing class data with keys:
                - id (int): Class ID
                - class_name (str): Class name
                - max_students_per_team (int): Max students per team
        """
        return {
            "id": self.id,
            "class_name": self.class_name,
            "max_students_per_team": self.max_students_per_team,
        }
