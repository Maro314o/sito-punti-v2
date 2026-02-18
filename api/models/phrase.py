from api.database import db


class Phrase(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    phrase: str = db.Column(db.Text, nullable=False)
    event_id: int = db.Column(db.Integer, db.ForeignKey("event.id"))

    @classmethod
    def get_by_id(cls, event_id: int) -> "Phrase":
        return cls.query.filter_by(id=event_id).one()

