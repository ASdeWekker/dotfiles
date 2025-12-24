"""
Check the size of the disk and notify the user if there's not much space left.
"""


import os
import psutil
import redis
import requests as req
from datetime import datetime
from dotenv import load_dotenv
# Service
import services.telegram_apprise as telmes


load_dotenv()


url = f"http://{os.uname()[1]}.local:8080/api/v2"
user = os.getenv("QBIT_USER")
pw = os.getenv("QBIT_PASS")
headers = {"Referer": f"http://{os.uname()[1]}.local:8080"}
redis = redis.Redis(host="localhost", port=6379, decode_responses=True)
REDIS_PREFIX = "CHDISP"  # CHeck DIsk SPace


def main():
    """ Everything comes together. """

    # Some more vars.
    min_space = 10  # Minimum amount of space that's acceptable in GB.
    speed_limit = 500  # The imposed speedlimit in KB/s.
    space_left = round(psutil.disk_usage("/")[2] / 1024 / 1024 / 1024)
    cookie = ""
    data = []

    # Set the last time the script ran.
    redis.set(f"{REDIS_PREFIX}_last_ran", str(datetime.now()))

    # Check if the script already limited the download speeds.
    get_download_limit = redis.get(f"{REDIS_PREFIX}_limit_set")
    download_limit_set = False if get_download_limit != "True" else True

    if download_limit_set is False:
        if space_left < min_space:
            print("Not enough space left.")

            # Login.
            res = req.post(
                url=f"{url}/auth/login",
                data={"username": user, "password": pw},
                headers=headers,
                timeout=10
            )

            if res.ok:
                print("Logged in!")
                cookie = res.headers["set-cookie"].split(";")[0].split("=")[1]
            else:
                print("Something went wrong while trying to login.")

            # Get list of torrents.
            res = req.get(
                url=f"{url}/torrents/info",
                headers=headers,
                cookies={"SID": cookie},
                    params={"filter": "all", "sort": "ratio"}
                    timeout=10
            )
            if res.ok:
                data = res.json()
            else:
                print("Something went wrong while grabbing the torrents. "
                      f"Status code: {res.status_code}.")

            # Slow the torrents down.
            params = {
                "hashes": "|".join([item["hash"] for item in data]),
                "limit": str(speed_limit * 1024)
            }

            res = req.post(
                url=f"{url}/torrents/setDownloadLimit",
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                cookies={"SID": cookie},
                data=params,
                timeout=10
            )

            if res.ok:
                print("Slowed the torrents down")
                telmes.message(
                    f"Slowed down the torrents to {speed_limit} KB/s")
            else:
                print(f"Status code: {res.status_code}")
                print(res.text)
                telmes.message(
                    "Something went wrong while trying to slow down.")

            # Logout again.
            res = req.post(
                url=f"{url}/auth/logout",
                headers=headers,
                cookies={"SID": cookie},
                timeout=10
            )

            if res.ok:
                print("Logged out again.")
            else:
                print("Something went wrong while trying to logout.")
        else:
            print(f"Enough space left: {space_left}GB. "
                  f"threshold is {min_space}GB. Skipping...")
    else:
        print("The download limit has been set, please fix disk issues "
              "and remove the limit.")


if __name__ == "__main__":
    main()
