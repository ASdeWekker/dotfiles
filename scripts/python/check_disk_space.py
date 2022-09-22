"""
Check the size of the disk and notify the user if there's not much space left.
"""


import apprise
import psutil
from dotenv import load_dotenv


load_dotenv()

bot_token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")
appr = apprise.Apprise()
appr.add(f"tgram://{bot_token}/{chat_id}")

min_space = 130 # Minimum amount of space that's acceptable
space_left = round(psutil.disk_usage("/")[2] / 1024 / 1024 / 1024)


if space_left < min_space:
    appr.notify(body=f"Minder dan {min_space}GB beschikbaar pik")
else:
    print("nu heb ik niks te zeggen")
