"""
Python code with mosh xxargs
"""


def main():
    """ Function """

    def save_user(**user):
        print(user)

    save_user(id=1, name="Alex", age=22)


if __name__ == "__main__":
    main()
