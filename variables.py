# data types
# numbers and strings


# add 2 numbers(only number can be added to number)

# print 2 + 3
# print 5 + int('6')
# print '4' + '5'



# scenarios for adding
def add(num1, num2):
    if num1 == "":
        num1 = 0
    if num2 == "":
        num2 = 0
    if num1 == None:
        num1 = 0
    if num2 == None:
        num2 = 0
    if type(num1) not in (int, str):
        return "Invalid number"
    return int(num1) + int(num2)

print add(1, 2)
print add("2", 3) # TypeError: cannot concatenate 'str' and 'int' objects
print add(4, '3')  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print add("", 3)  # ValueError: invalid literal for int() with base 10: ''
print add(45, "")  # ValueError: invalid literal for int() with base 10: ''
print add(None, 45) # TypeError: int() argument must be a string or a number, not 'NoneType'
print add(43, None) # TypeError: int() argument must be a string or a number, not 'NoneType'


# Try following scenarios
print add([1,2,3], 32)
