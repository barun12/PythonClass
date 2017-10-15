"""
simple calculator with file IO
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
    # list of possible operator signs
    signs = ["+", "-", "*", "/"]
    output_file_path = "./IOFiles/output.txt"
    with open("./IOFiles/input.txt", "r") as input_file, open(output_file_path, "w") as output_file:
        print "Writing output to file: {}".format(output_file_path)
        # read file line by line
        l = input_file.readline()
        # execute this till we read all the lines
        while l:
            # iterate over all operators
            for sign in signs:
                try:
                    num1, num2 = l.split(sign)
                except:
                    continue
                # typecast both numbers to integer, strip to remove extra spaces(if any)
                num1 = int(num1.strip())
                num2 = int(num2.strip())
                if sign == "+":
                    res = addition(num1, num2)
                    res_str = "{} + {} = {}".format(num1, num2, res)
                elif sign == "-":
                    res = subtraction(num1, num2)
                    res_str = "{} - {} = {}".format(num1, num2, res)
                elif sign == "*":
                    res = multiplication(num1, num2)
                    res_str = "{} * {} = {}".format(num1, num2, res)
                elif sign == "/":
                    res = devision(num1, num2)
                    res_str = "{} / {} = {}".format(num1, num2, res)
            output_file.write(res_str + "\n")
            l = input_file.readline()