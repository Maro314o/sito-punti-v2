from api.database import db
from api.constants import Weapon


class Power(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    user_id: int = db.Column(db.Integer, db.ForeignKey("user.id"))
    role: str = db.Column(db.String(150))
    powers_bitmask: int = db.Column(db.Integer, default=0)

    def is_power_avalidable(self) -> bool:
        return (self.powers_bitmask & 1) != 0

    def is_weapon_avalidable(self, weapon: Weapon) -> bool:
        return (self.powers_bitmask & weapon.value) != 0

    def use_weapon(self, weapon: Weapon) -> bool:
        if self.is_weapon_avalidable(weapon):
            self.powers_bitmask ^= weapon.value
            return True
        return False

    def reset_weapon_use(self, weapon: Weapon) -> None:
        self.powers_bitmask |= weapon.value

    @classmethod
    def get_by_id(cls, event_id: int) -> "Power":
        return cls.query.filter_by(id=event_id).one()
