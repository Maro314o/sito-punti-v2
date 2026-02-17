from pathlib import Path

API_DIRECTORY: Path = Path(__file__).parent
PROJECT_FOLDER: Path = API_DIRECTORY.parent
DOTENV_FILE: Path = PROJECT_FOLDER / ".env"
