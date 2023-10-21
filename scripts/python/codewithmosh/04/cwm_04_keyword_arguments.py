"""
Python code with mosh keyword arguments
"""


def main():
    """ Function """

    def increment(number, by):
        return number + by
    
    print(increment(2, by=1))


if __name__ == "__main__":
    main()
