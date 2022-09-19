"""
Check if there are updates and notify.
"""


import apprise
import os
import subprocess
from dotenv import load_dotenv


load_dotenv()

bot_token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")
appr = apprise.Apprise()
appr.add(f"tgram://{bot_token}/{chat_id}?silent=yes")

cupdates = subprocess.run(["checkupdates"], capture_output=True)
updates = int(subprocess.run(["wc", "-l"], input=cupdates.stdout, capture_output=True).stdout)
print(updates)

if updates == 1:
    appr.notify(body="There's 1 new update", title="Update")
elif updates > 0:
    appr.notify(body=f"There are {updates} new updates", title="Updates")
