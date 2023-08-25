"""
    Check if there are updates and notify.
    File will be executed via a cronjob.

    Currently works on: serge, piet
"""


import os
import subprocess
# Service
import services.telegram_apprise as telmes


host = os.uname()[1]
command = ""


def main():
    if host == "serge":
        command = ["checkupdates"]
    elif host == "piet":
        command = ["apt-get",
                "-q",
                "-y",
                "--ignore-hold",
                "--allow-change-held-packages",
                "--allow-unauthenticated",
                "-s",
                "dist-upgrade"]

    pre_updates = subprocess.run(command, capture_output=True)
    if host == "piet":
        pre_updates = subprocess.run(
            ["/bin/grep",  "^Inst"],
            input=pre_updates.stdout,
            capture_output=True
        )
    updates = int(subprocess.run(
        ["wc", "-l"],
        input=pre_updates.stdout,
        capture_output=True
    ).stdout)

    print(f"There is/are {updates} update(s) available.")

    if updates == 1:
        telmes.message(f"{host.capitalize()} has 1 new update 🥸")
    elif updates > 0:
        telmes.message(f"{host.capitalize()} has {updates} new updates 🥸")
    elif updates == 0:
        telmes.message("No new updates today 😢")


if __name__ == "__main__":
    main()
