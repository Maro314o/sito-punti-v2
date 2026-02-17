from api.database import db


class Classe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_classe = db.Column(db.String(150), unique=True)
    massimo_studenti_squadra = db.Column(db.Integer)

    squadre = db.relationship("Squadra", lazy="dynamic", backref="classe")
    studenti = db.relationship("Utente", lazy="dynamic", backref="classe")

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_by_nome(cls, nome_classe):
        return cls.query.filter_by(nome_classe=nome_classe).first()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_all_student_classes(cls):
        NOT_AVALIDABLE = frozenset(["admin", "Nessuna_squadra"])
        return cls.query.filter(Classe.nome_classe.notin_(NOT_AVALIDABLE)).all()

    def to_dict(self):
        return {
            "id": self.id,
            "nome_classe": self.nome_classe,
            "massimo_studenti_squadra": self.massimo_studenti_squadra,
        }
