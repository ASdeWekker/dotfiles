"""
	A service to easily send Telegram messages via Apprise.
"""


import apprise
import os
import sys
from dotenv import load_dotenv


load_dotenv()

user_message = sys.argv[1] if len(sys.argv) > 1 else ""
bot_token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")
appr = apprise.Apprise()
appr.add(f"tgram://{bot_token}/{chat_id}")


def message(message):
    """ Craft the message. """

    print(message)
    appr.notify(body=message)


def main():
    """ Actually send the message. """

    message(user_message)


if __name__ == "__main__":
    main()
