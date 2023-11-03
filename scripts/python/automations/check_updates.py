"""
    Check if there are updates and notify.
    File will be executed via a cronjob.

    Currently works on: serge, piet
"""


import os
import subprocess
# Service
import services.telegram_apprise as telmes


host = os.uname()[1].capitalize()
command = ""


def main():
    if host == "Serge":
        command = ["checkupdates"]
    elif host == "Piet":
        command = "apt-get -q -y --ignore-hold --allow-change-held-packages \
            --allow-unauthenticated -s dist-upgrade".split()

    pre_updates = subprocess.run(command, capture_output=True)
    if host == "Piet":
        pre_updates = subprocess.run(
            "/bin/grep ^Inst".split(),
            input=pre_updates.stdout,
            capture_output=True
        )
    updates = int(subprocess.run(
        "wc -l".split(),
        input=pre_updates.stdout,
        capture_output=True
    ).stdout)

    print(f"There is/are {updates} update(s) available.")

    if updates == 1:
        telmes.message(f"{host} has 1 new update 🥸")
    elif updates > 0:
        telmes.message(f"{host} has {updates} new updates 🥸")
    elif updates == 0:
        telmes.message(f"No new updates for {host} today 😢")


if __name__ == "__main__":
    main()
