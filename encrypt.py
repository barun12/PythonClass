"""
Assignment
"""

def encrypt(input_str):
    """
    :param input_str: "Hello"
    :return: "Igopt"
    """
    chars = list(input_str)   #["H", "e", "l", "l", "o"]
    out_str = ""
    for i in range(len(chars)):
        c = ord(chars[i])
        r = c + i + 1
        out_str = out_str + chr(r)

    return out_str





print encrypt("Zello")


def decrypt(input_str):
    """
    :param input_str: "Igopt
    :return: "Hello"
    """
    pass