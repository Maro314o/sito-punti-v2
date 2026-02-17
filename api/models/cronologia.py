from api.database import db


class Cronologia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(150))
    stagione = db.Column(db.Integer)
    attivita = db.Column(db.String(150))
    modifica_punti = db.Column(db.Float)

    utente_id = db.Column(db.Integer, db.ForeignKey("utente.id"))

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_utente(cls, utente_id):
        return cls.query.filter_by(utente_id=utente_id).all()

    @classmethod
    def get_by_utente_stagione(cls, utente_id, stagione):
        return cls.query.filter_by(utente_id=utente_id, stagione=stagione).all()

    @classmethod
    def get_by_stagione(cls, stagione):
        return cls.query.filter_by(stagione=stagione).all()

    def to_dict(self):
        return {
            "id": self.id,
            "data": self.data,
            "stagione": self.stagione,
            "attivita": self.attivita,
            "modifica_punti": self.modifica_punti,
            "utente_id": self.utente_id,
        }
