# 1. Create a class Complex Number with data members as real and imag and add
# following methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator

class Complex:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real,
                       self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real,
                       self.imag - other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

    def __del__(self):
        print("Complex Number object destroyed")


c1 = Complex(3, 4)
c2 = Complex(5, 2)

print("First Complex Number :", c1)
print("Second Complex Number :", c2)

c3 = c1 + c2
print("Addition :", c3)

c4 = c1 - c2
print("Subtraction :", c4)