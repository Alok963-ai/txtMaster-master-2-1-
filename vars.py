from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "20288951"))
API_HASH = getenv("API_HASH", "e8cb5fb7a475b5f5eb3b0ef0e6ca03a8")
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = int(getenv("OWNER_ID", "7833842279"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7833842279").split()))

