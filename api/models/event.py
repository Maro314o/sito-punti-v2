from api.database import db
import datetime


class Event(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    date: datetime.datetime = db.Column(db.DateTime, nullable=False)
    event_type: str = db.Column(db.String(150))
    event_variation: str = db.Column(db.String(150))
    season = db.Column(db.Integer)
    points: float = db.Column(db.Float)
    variation: str = db.Column(db.String(150))
    user_id: int = db.Column(db.Integer, db.ForeignKey("user.id"))

    @classmethod
    def get_by_id(cls, event_id: int) -> "Event":
        return cls.query.filter_by(id=event_id).one()
