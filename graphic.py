import math
from typing import Protocol


class Shape(Protocol):
    @property
    def area(self) -> float: ...

    @property
    def perimeter(self) -> float: ...


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    @property
    def area(self):
        return math.pi * (math.pow(self.radius, 2))

    @property
    def perimeter(self):
        return math.pi * (2 * self.radius)


class Parallelogram(Shape):
    def __init__(self, length: float, width: float, height: float):
        self.length = length
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.length * self.height

    @property
    def perimeter(self):
        return (self.length + self.width) * 2


class Rectangle(Parallelogram):
    def __init__(self, length: float, width: float):
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


class Square(Rectangle):
    def __init__(self, length: float):
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


class Triangle(Shape):
    def __init__(self, a: float, height: float, b: float, c: float):
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


class Trapezoid(Shape):
    def __init__(self, a: float, b: float, height: float, c: float, d: float):
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
