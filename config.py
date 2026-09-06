import os
from dotenv import load_dotenv


load_dotenv()


TELEGRAM_TOKEN = os.getenv(
    "TELEGRAM_TOKEN"
)

GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY"
)

DEEPSEEK_API_KEY = os.getenv(
    "DEEPSEEK_API_KEY"
)
