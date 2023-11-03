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


def redis_init():
    """ Initialize Redis and set some variables. """

    print("initialize redis")

def qbit_get_auth_cookie():
    """ Get the cookie used to authenticate future qbit Api requests. """

    user = os.getenv("QBIT_USER")
    pw = os.getenv("QBIT_PASS")
    url = f"http://{os.uname()[1]}.local:8080"

    print(url) # redis_init()

    res = req.post(
        url=f"{url}/api/v2/auth/login",
        data={"username": user, "password": pw},
        headers={"Referer": url}
    )
    print(f"{url}/api/v2/auth/login")
    return res.headers["set-cookie"].split(";")[0].split("=")[1]


def main():
    """ Everything comes together. """

    min_space = 50 # Minimum amount of space that's acceptable
    space_left = round(psutil.disk_usage("/")[2] / 1024 / 1024 / 1024)
    
    print(space_left)

    qbit_cookie = qbit_get_auth_cookie()
    print(qbit_cookie)

    # if space_left < min_space:
    #     qbit_cookie = qbit_get_auth_cookie()

    #     res = req.post()
        
    #     print(f"Not enough space available: {space_left}GB")
    #     telmes.message(f"Serge has less than {min_space}GB available, \
    #         the download speed has been set to 500 KB/s")
    # else:
    #     print(f"Enough space available: {space_left}GB")


if __name__ == "__main__":
    main()
