import os

from pathlib import Path
from dotenv import load_dotenv

# Project root directory

BASE_DIR = Path(__file__).resolve().parent.parent

# Load variables from the .env file

load_dotenv(BASE_DIR / ".env")

# Application configuration

TIMEFRAME = os.getenv("TIMEFRAME", "5m")

EMA_FAST = int(os.getenv("EMA_FAST", "9"))
EMA_SLOW = int(os.getenv("EMA_SLOW", "21"))

SYMBOL = os.getenv("SYMBOL", "^NSEI")
PERIOD = os.getenv("PERIOD", "5d")
# Email configuration
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")
MARKET_START = os.getenv("MARKET_START", "09:30")

MARKET_END = os.getenv("MARKET_END", "15:00")
