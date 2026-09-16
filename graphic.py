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


class Parallelogram(_BaseShape):
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.length * self.height

    @property
    def perimeter(self):
        return self.length * 2 + self.width * 2


class Rectangle(Parallelogram, _BaseShape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width

    @property
    def perimeter(self):
        return (self.length + self.width) * 2

    # 长方形是一种特殊的平行四边形，对吧。。
    @property
    def height(self):
        return self.width


class Square(Rectangle, _BaseShape):
    def __init__(self, length):
        self.length = length

    @property
    def area(self):
        return self.length**2

    @property
    def perimeter(self):
        return 4 * self.length

    # 正方形是一种特殊的长方形，对吧。。
    @property
    def width(self):
        return self.length


class Triangle(_BaseShape):
    def __init__(self, a, height, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.height = height

    @property
    def area(self):
        return self.a * self.height / 2

    @property
    def perimeter(self):
        return self.a + self.b + self.c


class Trapezoid(_BaseShape):
    def __init__(self, a, b, height, c, d):
        self.a = a
        self.b = b
        self.height = height
        self.c = c
        self.d = d

    @property
    def area(self):
        return (self.a + self.b) * self.height / 2

    @property
    def perimeter(self):
        return self.a + self.b + self.c + self.d
