import os
from pathlib import Path
from dotenv import load_dotenv

# Get the base directory
BASE_DIR = Path(__file__).resolve().parent

# Path to the .env file
ENV_PATH = BASE_DIR / '.env'

# Load the .env file
if ENV_PATH.exists():
    load_dotenv(ENV_PATH)
else:
    raise FileNotFoundError(f".env file not found at {ENV_PATH}")
