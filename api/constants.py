from pathlib import Path
from enum import Enum


# use this naming convention: _DIRECTORY for a folder/directory and _FILE for a file
API_DIRECTORY: Path = Path(__file__).parent
PROJECT_DIRECTORY: Path = API_DIRECTORY.parent
DOTENV_FILE: Path = PROJECT_DIRECTORY / ".env"
DATA_DIRECTORY: Path = PROJECT_DIRECTORY / "data"
DATABASE_FILE: Path = DATA_DIRECTORY / "database.db"


class Weapon(int, Enum):
    Poseidon = 1 << 1
    Pluton = 1 << 2
    Uranos = 1 << 3


WEAPONS = {
    Weapon.Poseidon: "Scelta argomento di una domanda dell’interrogazione",
    Weapon.Pluton: "Raddoppia taglia voto",
    Weapon.Uranos: "Sposta interrogazione a prossima data (+10 per anticipo)",
}
RESET_WEAPONS_BITMASK = 1
for i, _ in enumerate(WEAPONS):
    RESET_WEAPONS_BITMASK |= 1 << (i + 1)
