"""
Python code with mosh list unpacking
"""


def main():
    """ Function """

    numbers = [1, 2, 3]
    first, second, third = numbers

    more_numbers = [4, 5, 6, 7, 8]
    fourth, fifth, *other = more_numbers

    print(first)
    print(second)
    print(third)

    print(fourth)
    print(fifth)
    print(other)


if __name__ == "__main__":
    main()
