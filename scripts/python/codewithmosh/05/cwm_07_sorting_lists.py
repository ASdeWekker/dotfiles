"""
Python code with mosh sorting lists
"""


def main():
    """ Function """

    # numbers = [3, 51, 2, 8, 6]
    # numbers.sort(reverse=True)
    # sorted_numbers = sorted(numbers)
    # print(numbers)
    # print(sorted_numbers)

    items = [
        ("Product1", 10),
        ("Product2", 9),
        ("Product3", 12),
    ]

    def sort_item(item):
        return item[1]

    items.sort(key=sort_item)
    print(items)


if __name__ == "__main__":
    main()
