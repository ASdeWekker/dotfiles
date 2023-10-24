"""
Python code with mosh lambda functions
"""


def main():
    """ Function """

    items = [
        ("Product1", 10),
        ("Product2", 9),
        ("Product3", 12),
    ]

    items.sort(key=lambda item: item[1])
    print(items)


if __name__ == "__main__":
    main()
