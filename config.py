import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable not set")

BOT_USERNAME = "Mosteb_bot"
ADMIN_ID = [1515018212]
DEVELOPER_ID = [1677710142]