"""
Python code with mosh conditional statements
"""


def main():
    """ Function """

    temperature = 15
    if temperature > 30:
        print("It's warm")
        print("Drink water")
    elif temperature > 20:
        print("It's nice")
    else:
        print("It's cold")
    print("Done")


if __name__ == "__main__":
    main()
