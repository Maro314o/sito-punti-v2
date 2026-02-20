from pathlib import Path
from enum import Enum


# use this naming convention: _DIRECTORY for a folder/directory and _FILE for a file
API_DIRECTORY: Path = Path(__file__).parent
PROJECT_DIRECTORY: Path = API_DIRECTORY.parent
DOTENV_FILE: Path = PROJECT_DIRECTORY / ".env"
DATA_DIRECTORY: Path = PROJECT_DIRECTORY / "data"
DATABASE_FILE: Path = DATA_DIRECTORY / "database.db"


class Weapon(int, Enum):
    Poseidon = 1 << 0
    Pluton = 1 << 1
    Uranos = 1 << 2


WEAPONS = {
    Weapon.Poseidon: "Scelta argomento di una domanda dell’interrogazione",
    Weapon.Pluton: "Raddoppia taglia voto",
    Weapon.Uranos: "Sposta interrogazione a prossima data (+10 per anticipo)",
}
RESET_POWERS_BITMASK= 0
for i, _ in enumerate(WEAPONS):
    RESET_POWERS_BITMASK|= 1 << i 


class Role(str, Enum):
    Capitano = 1<<0
    Navigatore = 1<<1
    Carpentiere =1<<2
    Medico =1<<3
    Cecchino =1<<4
    Sguattero =1<<5


ROLES = {
    Role.Capitano: {
        "power_name": "Ambizione del Re Conquistatore",
        "power_description": "Può annullare max -10 (no voti)",
    },
    Role.Navigatore: {
        "power_name": "Ambizione della Percezione",
        "power_description": "Può spostare punti max 5 (no voti e sotto 0)",
    },
    Role.Carpentiere: {
        "power_name": "Albero Adam",
        "power_description": "Può annullare max -4 (no voti)",
    },
    Role.Medico: {
        "power_name": "Voce di Tutte le Cose",
        "power_description": "Può raddoppiare bonus (no voti)",
    },
    Role.Cecchino: {
        "power_name": "Ambizione degli Armamenti",
        "power_description": "Può dimezzare malus",
    },
    Role.Sguattero: {
        "power_name": "Pulisci pavimento",
        "power_description": "Pulisce il pavimento",
    },
}

class EventType(str, Enum):
    pass

