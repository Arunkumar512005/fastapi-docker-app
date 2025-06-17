from loguru import logger
from datetime import datetime
import jwt
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

# ✅ Logs requests to a file
logger.add("logs/api.log", rotation="500 KB")

def log_request(user: str, text: str):
    logger.info(f"User: {user} | Text: {text} | Time: {datetime.now()}")