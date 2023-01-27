"""
Check if there are updates and notify.
File will be executed via a cronjob.

Currently works on: serge, piet
"""


import apprise
import os
import subprocess
from dotenv import load_dotenv


load_dotenv()

bot_token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")
host = os.uname()[1]
command = ""
appr = apprise.Apprise()
appr.add(f"tgram://{bot_token}/{chat_id}")

if host == "serge":
    command = "checkupdates"
elif host == "piet":
    command = "aptitude search \"~U\""

pre_updates = subprocess.run([command], capture_output=True)
updates = int(subprocess.run(
    ["wc", "-l"],
    input=pre_updates.stdout,
    capture_output=True
).stdout)

print(updates)

if updates == 1:
    appr.notify(body=f"{host.capitalize()} has 1 new update 🥸")
elif updates > 0:
    appr.notify(body=f"{host.capitalize()} has {updates} new updates 🥸")
