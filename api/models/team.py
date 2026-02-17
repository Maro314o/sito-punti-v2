from api.database import db
from sqlalchemy import func


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    number_of_components= db.Column(db.Integer)

    studenti_componenti = db.relationship(
        "Utente", lazy="dynamic", backref="team"
    )

    classe_id = db.Column(db.Integer, db.ForeignKey("classe.id"))

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_by_nome(cls, nome_squadra):
        return cls.query.filter_by(nome_squadra=nome_squadra).first()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_classe(cls, classe_id):
        return cls.query.filter_by(classe_id=classe_id).all()

    def punti_stagione(self, stagione):
        from api.models.cronologia import Cronologia
        from api.models.classe import Classe

        id_utenti_squadra = [studente.id for studente in self.studenti_componenti.all()]

        if not id_utenti_squadra:
            return 0

        punti_squadra = db.session.scalar(
            db.select(func.coalesce(func.sum(Cronologia.modifica_punti), 0)).where(
                Cronologia.utente_id.in_(id_utenti_squadra),
                Cronologia.stagione == stagione,
            )
        )

        classe = Classe.get_by_id(self.classe_id)
        if not classe or not classe.massimo_studenti_squadra:
            return punti_squadra

        return punti_squadra * (
            classe.massimo_studenti_squadra / len(id_utenti_squadra)
        )

    def to_dict(self):
        return {
            "id": self.id,
            "nome_squadra": self.nome_squadra,
            "numero_componenti": self.numero_componenti,
            "classe_id": self.classe_id,
        }
