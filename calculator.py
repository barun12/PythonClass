"""
simple calculator
author: Barun Kumar Sharma(barun12)
"""

def addition(num1, num2):
    """
    :param num1: 1st number
    :param num2: 2nd number
    :return: sum of num1 and num2
    """
    return num1 + num2


def subtraction(num1, num2):
    """
    :param num1: 1st number
    :param num2: 2nd number
    :return: subtraction of num2 from num1
    """
    return num1 - num2


def multiplication(num1, num2):
    """
    :param num1: 1st number
    :param num2: 2nd number
    :return: multiplication of num1 and num2
    """
    return num1 * num2


def devision(num1, num2):
    """
    :param num1: 1st number, numerator
    :param num2: 2nd number, denominator
    :return: division of num1 and num2
    """
    return num1 / num2


if __name__ == "__main__":
    # num1 is user input which will be typecaster to integer
    num1 = int(raw_input("Enter 1st number: "))
    # num2 is also user input but we can get integer directly, type cast not required
    num2 = input("Enter 2nd number: ")

    res = addition(num1, num2)
    print "{} + {} = {}".format(num1, num2, res)

    res = subtraction(num1, num2)
    print "{} - {} = {}".format(num1, num2, res)

    res = multiplication(num1, num2)
    print "{} * {} = {}".format(num1, num2, res)

    res = devision(num1, num2)
    print "{} / {} = {}".format(num1, num2, res)
