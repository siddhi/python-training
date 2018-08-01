import math

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def abs(self):
        return math.sqrt(self.real**2 + self.imag**2)

    def angle(self):
        return math.degrees(math.atan(self.imag / self.real))

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return Complex(self.real*other.real - self.imag*other.imag,
                       self.real*other.imag + self.imag*other.real)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __gt__(self, other):
        return self.abs() > other.abs()

    def __str__(self):
        return "{} + {}i".format(self.real, self.imag)

if __name__ == "__main__":
    print(Complex(2, 4))
