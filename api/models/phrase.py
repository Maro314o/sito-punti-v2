from api.database import db


class Phrase(db.Model):
    """
    Phrase model representing a motivational phrase.

    Attributes:
        id (int): Primary key
        phrase (str): The motivational phrase text
        event_id (int): Foreign key to the event table

    Relationships:
        event (relationship): Many-to-one relationship with Event model
    """

    id: int = db.Column(db.Integer, primary_key=True)
    phrase: str = db.Column(db.Text, nullable=False)
    event_id: int = db.Column(db.Integer, db.ForeignKey("event.id"), nullable=True)

    @classmethod
    def get_by_id(cls, phrase_id: int) -> "Phrase":
        """
        Retrieve a phrase by its ID.

        Args:
            phrase_id (int): The unique identifier of the phrase.

        Returns:
            Phrase: The phrase object with the specified ID.

        Raises:
            NoResultFound: If no phrase with the given ID exists.
        """
        return cls.query.filter_by(id=phrase_id).one()

    @classmethod
    def get_by_event(cls, event_id: int) -> "Phrase | None":
        """
        Retrieve a phrase associated with a specific event.

        Args:
            event_id (int): The ID of the event.

        Returns:
            Phrase | None: The phrase object if found, None otherwise.
        """
        return cls.query.filter_by(event_id=event_id).first()

    @classmethod
    def get_all(cls) -> list["Phrase"]:
        """
        Retrieve all phrases.

        Returns:
            list[Phrase]: List of all phrases.
        """
        return cls.query.all()
