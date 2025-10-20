import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

ADMIN_IDS = [int(admin_id) for admin_id in os.getenv("ADMIN_IDS", "").split(",") if admin_id]

FREE_LIMIT_MESSAGES = 10
PRO_PRICE_STARS = 100  
ULTRA_PRICE_STARS = 250


DB_URL = "sqlite+aiosqlite:///database/users.db" 
# PostgreSQL:
# DB_URL = "postgresql+asyncpg://user:pass@host/db_name"