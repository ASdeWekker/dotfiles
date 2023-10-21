"""
Python code with mosh default arguments
"""


def main():
    """ Function """
    # can't add another required parameter after a default one.
    def increment(number, by=1):
        return number + by

    print(increment(2, 5))


if __name__ == "__main__":
    main()
