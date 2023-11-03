"""
	This will serve as a wrapper for snapraid.
    The main purpose is to make sure it does not run when an error has been
    detected in the array.
"""


import subprocess


command = "snapraid status".split()


def main():
    proc = str(subprocess.run(command, capture_output=True).stdout).split("\\n")
    print(proc[len(proc)-2])


if __name__ == "__main__":
    main()
