from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        raise NotImplementedError


class Cerc(Shape):
    def __init__(self, raza):
        self.raza = raza

    def calculate_area(self):
        return math.pi * self.raza**2

    def calculate_perimeter(self):
        return 2*(math.pi * self.raza)


class Dreptunghi(Shape):
    def __init__(self, lungime, latime):
        self.lungime = lungime
        self.latime = latime

    def calculate_area(self):
        return self.lungime * self.latime

    def calculate_perimeter(self):
        return 2 * self.lungime + 2 * self.latime


class Patrat(Dreptunghi):
    def __init__(self, lungime):
        self.lungime = lungime
        self.latime = lungime


class Triunghi(Shape):
    def __init__(self, l1, l2, l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

    def calculate_area(self):
        return (self.l1 * self.l2 * self.l3) / 2

    def calculate_perimeter(self):
        return self.l1 + self.l2 + self.l3


patrat1 = Patrat(5)

print(patrat1.calculate_area())
print(patrat1.calculate_perimeter())
