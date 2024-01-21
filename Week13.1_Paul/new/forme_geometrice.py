# Write a Python program to create a class that represents a shape.
# Include methods to calculate its area and perimeter.
# Implement subclasses for different shapes like circle, triangle, and rectangle
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def calculate_area(self) -> float:
        pass

    def calculate_perimeter(self) -> float:
        raise NotImplementedError()


class Circle(Shape):
    def __init__(self, raza):
        self.raza = raza

    def calculate_area(self) -> float:
        return pi*self.raza**2

    def calculate_perimeter(self) -> float:
        return 2*pi*self.raza


shape = Shape()
shape.calculate_area()
