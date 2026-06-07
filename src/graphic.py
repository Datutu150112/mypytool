import math
from . import main
class Circle():
    def __init__(self,radius):
        self.Radius = radius
        self.Area = math.pi * (main.pow(self.Radius,2))
        self.Perimeter = math.pi * (2 * self.Radius)
    def radius(self):
        return self.Radius
    def area(self):
        return self.Area
    def perimeter(self):
        return self.Perimeter   
    
class Square():
    def __init__(self,side_length):
        self.Side_length = side_length
        self.Perimeter = 4 * side_length
        self.Area = side_length * side_length
    def side_length(self):
        return self.Side_length
    def area(self):
        return self.Area
    def perimeter(self):
        return self.Perimeter
    
class Rectangle():
    def __init__(self,Length, Width):
        self.Length = Length
        self.Width = Width
        self.Perimeter = (self.Length + self.Width) * 2
        self.Area = self.Length * self.Width
    def width(self):
        return self.Width
    def length(self):
        return self.Length
    def area(self):
        return self.Area
    def perimeter(self):
        return self.Perimeter
    
class Triangle():
    def __init__(self,a,h,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.h = h
        self.Area = a * h / 2
        self.Perimeter = a + b + c
    def alen(self):
        return self.a
    def blen(self):
        return self.b
    def clen(self):
        return self.c
    def high(self):
        return self.h
    def area(self):
        return self.Area
    def perimeter(self):
        return self.Perimeter

class Parallelogram():
    def __init__(self,a,b,h):
        self.a = a
        self.b = b
        self.h = h
        self.Area = a * h
        self.Perimeter = a*2 + b*2
    def alen(self):
        return self.a
    def blen(self):
        return self.b
    def hlen(self):
        return self.h
    def area(self):
        return self.Area
    def perimeter(self):
        return self.Perimeter

class Trapezoid():
    def __init__(self,a,b,h,c,d):
        self.a = a
        self.b = b
        self.h = h
        self.c = c
        self.d = d
        self.Area = (a + b) * h / 2
        self.Perimeter = a + b + c + d
    def alen(self):
        return self.a
    def blen(self):
        return self.b
    def hlen(self):
        return self.h
    def clen(self):
        return self.c
    def dblen(self):
        return self.d
    def area(self):
        return self.Area
    def perimeter(self):
        return self.Perimeter

