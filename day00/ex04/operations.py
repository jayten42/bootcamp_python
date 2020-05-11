import sys


def get_sum(num1, num2):
    return num1 + num2


def get_difference(num1, num2):
    return num1 - num2


def get_product(num1, num2):
    return num1 * num2


def get_quotient(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "ERROR (div by zero)"


def get_remainder(num1, num2):
    try:
        return num1 % num2
    except ZeroDivisionError:
        return "ERROR (modulo by zero)"


def run(num1, num2):
    print("Sum:\t\t", get_sum(num1, num2))
    print("Difference:\t", get_difference(num1, num2))
    print("Product:\t", get_product(num1, num2))
    print("Quotient:\t", get_quotient(num1, num2))
    print("Remainder:\t", get_remainder(num1, num2))


if __name__ == '__main__':
    if len(sys.argv) < 3:
        quit("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
    elif len(sys.argv) > 3:
        print("InputError: too many arguments")
        quit("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
    try:
        num1, num2 = map(int, sys.argv[1:])
        run(num1, num2)
    except ValueError:
        print("InputError: only numbers")
        quit("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")


