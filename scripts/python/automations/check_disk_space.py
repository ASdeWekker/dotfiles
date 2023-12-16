"""
Check the size of the disk and notify the user if there's not much space left.
"""


import os
import psutil
import requests as req
from dotenv import load_dotenv
# Service
import services.telegram_apprise as telmes


load_dotenv()


url = f"http://{os.uname()[1]}.local:8080/api/v2"


def redis_init():
    """ Initialize Redis and set some variables. """

    print("initialize redis")


def qbit_get_auth_cookie():
    """ Get the cookie used to authenticate future qbit Api requests. """

    user = os.getenv("QBIT_USER")
    pw = os.getenv("QBIT_PASS")

    headers = {"Referer": url}

    res = req.post(
        url=f"{url}/auth/login",
        data={"username": user, "password": pw},
        headers=headers
    )

    if res.status_code == 200:
        print("Logged in!")
        return res.headers["set-cookie"].split(";")[0].split("=")[1]
    print("Something went wrong while trying to login.")


def torrent_list(filters, sort, reverse):
    """ Get a list of all the torrents currently in Qbit. """

    # cookies = {"SID": qbit_get_auth_cookie()}
    params = {
        "filter": filters,
        "sort": sort,
        "reverse": reverse,
    }

    res = req.get(
        url=f"{url}/torrents/info",
        # headers=headers,
        cookies={"SID": qbit_get_auth_cookie()},
        params=params
    )

    if res.status_code == 200:
        return res.json()


def logout():
    """ Logout once everything is done. """

    # cookies = {"SID": qbit_get_auth_cookie()}

    res = req.post(
        url=f"{url}/auth/logout",
        # headers=headers,
        cookies={"SID": qbit_get_auth_cookie()}
    )

    if res.status_code == 200:
        print("Logged out again.")
    else:
        print("Something went wrong while logging out.")


def main():
    """ Everything comes together. """

    min_space = 150  # Minimum amount of space that's acceptable in GB.
    speed_limit = 500  # The imposed speedlimit in KB/s.
    space_left = round(psutil.disk_usage("/")[2] / 1024 / 1024 / 1024)

    # torrents = torrent_list("all", "ratio", "false")

    if space_left < min_space:
        cookies = {"SID": qbit_get_auth_cookie()}
        torrents = torrent_list("all", "ratio", "false")
        params = {
            # "hashes": [torrent["hash"] for torrent in torrents].join("|"),
            "hashes": "|".join([torrent["hash"] for torrent in torrents]),
            "limit": speed_limit * 1024,
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        # for torrent in torrents:
        res = req.post(
            url=f"{url}/torrents/setDownloadLimit",
            headers=headers,
            cookies=cookies,
            params=params
        )

        # res = req.post(
        #     url=f"{url}/transfer/setDownloadLimit",
        #     data={"limit": speed_limit * 1024},
        #     headers=headers,
        #     cookies=cookies
        # )

        if res.status_code == 200:  # Not enough space.
            print(f"Not enough space available: {space_left}GB, "
                  f"limit is set to {min_space}GB.")
            telmes.message(f"Serge has less than {min_space}GB available, "
                           f"limit is set to {min_space}GB. The download "
                           f"speed has been set to {speed_limit} KB/s.")
        else:  # Something went wrong limiting the speed.
            print("Something went wrong :(")
            print(res.status_code)
            telmes.message("Something went wrong while trying to limit the "
                           "download speed.")
    else:  # Enough space available.
        print(f"Enough space available: {space_left}GB, "
              f"limit is set to {min_space}GB.")

    logout()


if __name__ == "__main__":
    main()
