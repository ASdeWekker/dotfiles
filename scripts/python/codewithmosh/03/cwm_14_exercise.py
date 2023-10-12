"""
Python code with mosh exercise
"""


def main():
    """ Function """

    count = 0
    for x in range(1, 10):
        if x % 2 == 0:
            print(x)
            count += 1
    print(f"We have {count} even numbers")


if __name__ == "__main__":
    main()
