"""
	A service to easily send Telegram messages via Apprise.
"""


import apprise
from dotenv import load_dotenv


load_dotenv

bot_token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")
appr = apprise.Apprise()
appr.add(f"tgram://{bot_token}/{chat_id}")


def message(message):
    appr.notify(body=message)
