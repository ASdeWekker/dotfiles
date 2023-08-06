"""
	This will serve as a wrapper for snapraid.
    The main purpose is to make sure it does not run when an error has been
    detected in the array.
"""


import os


snapraid = "snapraid"


def main():
    print(snapraid)


if __name__ == "__main__":
    main()
