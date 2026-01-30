#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math


# -------------------------
# Abstract Shape Class
# -------------------------
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# -------------------------
# Concrete Subclasses
# -------------------------
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# -------------------------
# Duck Typing Function
# -------------------------
def shape_info(shape):
    """
    Prints the area and perimeter of any object that behaves like a Shape.
    No type checking is done; relies on duck typing.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
