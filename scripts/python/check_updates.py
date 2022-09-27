"""
Check if there are updates and notify.
File will be executed via cronjob.
"""


import apprise
import os
import subprocess
from dotenv import load_dotenv


load_dotenv()

bot_token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")
appr = apprise.Apprise()
appr.add(f"tgram://{bot_token}/{chat_id}")

pre_updates = subprocess.run(["checkupdates"], capture_output=True)
updates = int(subprocess.run(["wc", "-l"], input=pre_updates.stdout, capture_output=True).stdout)
print(updates)

if updates == 1:
    appr.notify(body="Serge has 1 new update 🥸")
elif updates > 0:
    appr.notify(body=f"Serge has {updates} new updates 🥸")
