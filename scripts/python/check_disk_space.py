"""
Check the size of the disk and notify the user if there's not much space left.
"""


import apprise
import psutil


secret_string = "Located in an .env file"
min_space = 130 # Minimum amount of space that's acceptable
space_left = round(psutil.disk_usage("/")[2] / 1024 / 1024 / 1024)
appr = apprise.Apprise()
appr.add(f"tgram://{secret_string}?silent=yes")

if space_left < min_space:
    appr.notify(body=f"Minder dan {min_space}GB beschikbaar pik", title="Qbits")
else:
    print("nu heb ik niks te zeggen")
