import logging
from pydantic_settings import BaseSettings
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parent.parent
UPLOAD_FOLDER = PACKAGE_ROOT / 'uploads'
UPLOAD_FOLDER.mkdir(exist_ok=True)
LOG_DIR = PACKAGE_ROOT / 'logs'
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE =  LOG_DIR / 'pm_api.log'



ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

class LoggingSettings(BaseSettings):
    LOGGING_LEVEL: int = logging.INFO

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    # Meta
    logging: LoggingSettings = LoggingSettings()

    PROJECT_NAME: str = "Computer Vision Prediction API"

    class Config:
        case_sensitive = True


settings = Settings()