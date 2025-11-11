import os
import environ
from pathlib import Path

# Base directory = directory where manage.py is
BASE_DIR = Path(__file__).resolve().parent

# Initialize environment
env = environ.Env(
    DEBUG=(bool, False)
)

# Load .env file from the base directory
environ.Env.read_env(BASE_DIR / ".env")

# Environment variables
DEBUG = env("DEBUG")
SECRET_KEY = env("SECRET_KEY")
SIGNING_KEY = env("SIGNING_KEY")
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
