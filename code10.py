from math import *
class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)
    def __mul__(self, other):
        return Complex(self.real*other.real - self.imaginary*other.imaginary, self.imaginary*other.real + self.real*other.imaginary)
    def __truediv__(self, other):
        r = float(other.real**2 + other.imaginary**2)
        return Complex((self.real*other.real + self.imaginary*other.imaginary)/r, (self.imaginary*other.real - self.real*other.imaginary)/r)
    def mod(self):
        return Complex(sqrt(self.real**2 + self.imaginary**2), 0)
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result
x_r, x_i = map(float, input().split())
y_r, y_i = map(float, input().split())
x = Complex(x_r, x_i)
y = Complex(y_r, y_i)
print(x + y)
print(x - y)
print(x*y)
print(x/y)
print(x.mod())
print(y.mod())
