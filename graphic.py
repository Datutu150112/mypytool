import math

from typing import Protocol


class _BaseShape(Protocol):
    @property
    def area(self) -> float: ...

    @property
    def perimeter(self) -> float: ...


class Circle(_BaseShape):
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * (math.pow(self.radius, 2))

    @property
    def perimeter(self):
        return math.pi * (2 * self.radius)


class Square(_BaseShape):
    def __init__(self, length):
        self.length = length

    @property
    def area(self):
        return self.length**2

    @property
    def perimeter(self):
        return 4 * self.length


class Rectangle(_BaseShape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width

    @property
    def perimeter(self):
        return (self.length + self.width) * 2


class Triangle(_BaseShape):
    def __init__(self, a, h, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.height = h

    @property
    def area(self):
        return self.a * self.height / 2

    @property
    def perimeter(self):
        return self.a + self.b + self.c


class Parallelogram(_BaseShape):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    @property
    def area(self):
        return self.a * self.h

    @property
    def perimeter(self):
        return self.a * 2 + self.b * 2


class Trapezoid(_BaseShape):
    def __init__(self, a, b, h, c, d):
        self.a = a
        self.b = b
        self.h = h
        self.c = c
        self.d = d

    @property
    def area(self):
        return (self.a + self.b) * self.h / 2

    @property
    def perimeter(self):
        return self.a + self.b + self.c + self.d
