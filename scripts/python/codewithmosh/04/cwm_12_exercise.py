"""
Python code with mosh exercise
"""


def main():
    """ Function
        Divisible by 3 = fizz, 5 = buzz, 3 & 5 = fizzbuzz, else return num """

    def fizz_buzz(input):
        if input % 3 == 0 and input % 5 == 0:
            return "FizzBuzz"
        if input % 3 == 0:
            return "Fizz"
        if input % 5 == 0:
            return "Buzz"
        return input

    print(fizz_buzz(15))
    print(fizz_buzz(6))
    print(fizz_buzz(10))
    print(fizz_buzz(14))


if __name__ == "__main__":
    main()
