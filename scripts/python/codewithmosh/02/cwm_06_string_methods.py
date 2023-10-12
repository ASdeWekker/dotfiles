"""
Python code with mosh string methods
"""


def main():
    """ Function. """
    course = "python programming"

    print(course.upper())
    print(course.title())
    print(course.strip())
    print(course.find("pro"))
    print(course.replace("p", "J"))
    print("pro" in course.upper())
    print("swift" not in course)


if __name__ == "__main__":
    main()
