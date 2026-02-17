from flask_login import UserMixin
from sqlalchemy import func
from api.database import db


class Utente(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    nominativo = db.Column(db.String(150), unique=True)
    squadra = db.Column(db.String(150))
    password = db.Column(db.String(150))
    admin_user = db.Column(db.Integer, default=0)
    account_attivo = db.Column(db.Integer, default=0)

    classe_id = db.Column(db.Integer, db.ForeignKey("classe.id"))
    squadra_id = db.Column(db.Integer, db.ForeignKey("squadra.id"))

    cronologia_studente = db.relationship(
        "Cronologia", lazy="dynamic", backref="studente"
    )

    def is_admin(self):
        return self.admin_user == 1

    def is_active_account(self):
        return self.account_attivo == 1

    @classmethod
    def get_by_id(cls, user_id):
        return cls.query.filter_by(id=user_id).first()

    @classmethod
    def get_by_nominativo(cls, nominativo):
        return cls.query.filter_by(nominativo=nominativo).first()

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def get_all_students(cls):
        return cls.query.filter_by(admin_user=0).all()

    @classmethod
    def get_all_admins(cls):
        return cls.query.filter_by(admin_user=1).all()

    @classmethod
    def get_active_students(cls):
        return cls.query.filter_by(admin_user=0, account_attivo=1).all()

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "nominativo": self.nominativo,
            "squadra": self.squadra,
            "admin_user": self.admin_user,
            "account_attivo": self.account_attivo,
            "classe_id": self.classe_id,
            "squadra_id": self.squadra_id,
        }
