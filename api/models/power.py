from api.constants import RESET_POWERS_BITMASK, Role, Weapon
from api.database import db


class Power(db.Model):
    """
    Power model representing a user's powers and roles in the system.

    Uses bitmasks to store multiple roles, powers, and weapons.

    Attributes:
        id (int): Primary key
        user_id (int): Foreign key to the user table
        role_bitmask (int): Bitmask representing user's roles
        powers_bitmask (int): Bitmask representing available powers
        weapons_bitmask (int): Bitmask representing available weapons

    Note:
        Role bitmask values:
            - Capitano = 1<<0
            - Navigatore = 1<<1
            - Carpentiere = 1<<2
            - Medico = 1<<3
            - Cecchino = 1<<4
            - Sguattero = 1<<5
    """

    id: int = db.Column(db.Integer, primary_key=True)
    user_id: int = db.Column(db.Integer, db.ForeignKey("user.id"))
    role_bitmask: int = db.Column(db.Integer, default=0)
    powers_bitmask: int = db.Column(db.Integer, default=0)
    weapons_bitmask: int = db.Column(db.Integer, default=0)

    def is_power_available(self, power: Role) -> bool:
        """
        Check if a specific power is available.

        Args:
            power (Role): The role/power to check.

        Returns:
            bool: True if the power is available, False otherwise.
        """
        return (self.powers_bitmask & power.value) != 0

    def is_weapon_available(self, weapon: Weapon) -> bool:
        """
        Check if a specific weapon is available.

        Args:
            weapon (Weapon): The weapon to check.

        Returns:
            bool: True if the weapon is available, False otherwise.
        """
        return (self.powers_bitmask & weapon.value) != 0

    def use_weapon(self, weapon: Weapon) -> bool:
        """
        Use a weapon (marks it as used by toggling the bit).

        Args:
            weapon (Weapon): The weapon to use.

        Returns:
            bool: True if weapon was used, False if not available.
        """
        if self.is_weapon_available(weapon):
            self.powers_bitmask ^= weapon.value
            return True
        return False

    def reset_weapon_use(self, weapon: Weapon) -> None:
        """
        Reset a weapon's usage (makes it available again).

        Args:
            weapon (Weapon): The weapon to reset.
        """
        self.powers_bitmask |= weapon.value

    def reset_powers_use(self) -> None:
        """Reset all powers usage, making all powers available again."""
        self.powers_bitmask = RESET_POWERS_BITMASK

    @classmethod
    def get_by_id(cls, power_id: int) -> "Power":
        """
        Retrieve a power record by its ID.

        Args:
            power_id (int): The unique identifier of the power record.

        Returns:
            Power: The power object with the specified ID.

        Raises:
            NoResultFound: If no power record with the given ID exists.
        """
        return cls.query.filter_by(id=power_id).one()
