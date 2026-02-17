from pathlib import Path


# use this naming convention: _DIRECTORY for a folder/directory and _FILE for a file
API_DIRECTORY: Path = Path(__file__).parent
PROJECT_DIRECTORY: Path = API_DIRECTORY.parent
DOTENV_FILE: Path = PROJECT_DIRECTORY / ".env"
DATA_DIRECTORY: Path = PROJECT_DIRECTORY / "data"
DATABASE_FILE: Path = DATA_DIRECTORY / "database.db"
