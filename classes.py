"""
starting OOPS

"""

# class definition
# class Person:
#     def __init__(self, name, age, native_place):
#         self.name = name
#         self.age = age
#         self.native_place = native_place
#
#     def get_fullname(self, last_name):
#         return "{} {}".format(self.name, last_name)
#
#
# # instancec/object of class Person
# person_barun = Person("Barun", 28, "Pune")
#
#
# # accessing attributes of object
# print person_barun.name, person_barun.age, person_barun.native_place
# print person_barun.get_fullname("Sharma")


# Complex numbers (2 + 3i)
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return "Complex Number: {} + {}i".format(self.real, self.imag)

    def __add__(self, other_complex):
        real_part = self.real + other_complex.real
        imag_part = self.imag + other_complex.imag
        return Complex(real_part, imag_part)


complex1 = Complex(2, 3)
complex2 = Complex(4, 5)

print complex1 # <__main__.Complex instance at 0x7fbd42f80b90> without overriding __str__
print complex1 # Complex Number: 2 + 3i - after overriding __str__

print complex1 + complex2 # Complex Number: 6 + 8i



