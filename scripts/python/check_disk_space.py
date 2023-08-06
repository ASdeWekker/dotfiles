"""
Check the size of the disk and notify the user if there's not much space left.
"""


import apprise
import os
import psutil
import requests as req
from dotenv import load_dotenv


load_dotenv()


def apprise_init():
    """ Initialize the apprise integration. """

    bot_token = os.getenv("BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    appr = apprise.Apprise()
    appr.add(f"tgram://{bot_token}/{chat_id}")

    return appr

def redis_init():
    print("initialize redis")

def qbit_get_auth_cookie():
    """ Get the cookie used to authenticate future qbit Api requests. """

    user = os.getenv("QBIT_USER")
    pw = os.getenv("QBIT_PASS")
    url = f"http://{os.uname()[1]}.local:8080"
    res = req.post(
        url=f"{url}/api/v2/auth/login",
        data={"username": user, "password": pw},
        headers={"Referer": url}
    )
    return res.headers["set-cookie"].split(";")[0].split("=")[1]


def main():
    qbit_cookie = qbit_get_auth_cookie()
    appr = apprise_init()
    min_space = 50 # Minimum amount of space that's acceptable
    space_left = round(psutil.disk_usage("/")[2] / 1024 / 1024 / 1024)

    if space_left < min_space:
        res = req.post
        appr.notify(body=f"Serge has less than {min_space}GB available, \
            the download speed has been set to 500 KB/s")


if __name__ == "__main__":
    main()
