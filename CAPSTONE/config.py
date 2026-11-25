import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent

# Load environment variables from .env file
load_dotenv(BASE_DIR / ".env")


class Config:
    """Application configuration."""

    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-prompt-wise-ai-2026")

    # Database configuration - ensure database directory exists and resolve absolute path
    DB_DIR = BASE_DIR / "database"
    DB_DIR.mkdir(parents=True, exist_ok=True)
    DEFAULT_DB_PATH = (DB_DIR / "promptwise.db").as_posix()

    env_db_url = os.getenv("DATABASE_URL")
    if not env_db_url or "database/promptwise.db" in env_db_url:
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{DEFAULT_DB_PATH}"
    else:
        SQLALCHEMY_DATABASE_URI = env_db_url

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Gemini Generative AI Configuration
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
    GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
    MAX_TOKENS = int(os.getenv("MAX_TOKENS", "2048"))
    TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))

    # Adaptive Refinement Configuration
    MAX_REFINEMENT_ITERATIONS = int(os.getenv("MAX_REFINEMENT_ITERATIONS", "3"))
    QUALITY_THRESHOLD = float(os.getenv("QUALITY_THRESHOLD", "8.5"))


class TestingConfig(Config):
    """Testing configuration."""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    WTF_CSRF_ENABLED = False
