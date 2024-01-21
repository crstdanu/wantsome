from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Engine:
    """
    Class representing engine objects
    TODO complete the constructor and use it in the Automobil class instead of simple strings
    """
    def __init__(self, capacitate_cilindrica, combustibil, nr_cilindri):
        pass


class Chassis:
    """
    Class representing chassis objects
    TODO complete the constructor and use it in the Automobil class instead of simple strings
    """
    def __init__(self, cutie_de_viteze, transmisie, directie, awd=False):
        pass


class Coach:
    """
    Class representing Coach objects
    TODO complete the constructor and use it in the Automobil class instead of simple strings
    """
    def __init__(self, forma, nr_usi, trapa=False):
        pass


class Multimedia:
    """
    Class representing Multimedia car options
    TODO complete the constructor and optionally use it in the Automobil class
    """
    def __init__(self):
        pass


class CarBuilder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """
    @property
    @abstractmethod
    def product(self) -> Automobil:
        pass

    @abstractmethod
    def produce_engine(self) -> None:
        pass

    @abstractmethod
    def produce_chassis(self) -> None:
        pass

    @abstractmethod
    def produce_coach(self) -> None:
        pass


class Dacia(CarBuilder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """

    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """
        self.reset()

    def reset(self) -> None:
        self._product = Logan()

    @property
    def product(self) -> Logan:
        """
        Concrete Builders are supposed to provide their own methods for
        retrieving results. That's because various types of builders may create
        entirely different products that don't follow the same interface.
        Therefore, such methods cannot be declared in the base Builder interface
        (at least in a statically typed programming language).

        Usually, after returning the end result to the client, a builder
        instance is expected to be ready to start producing another product.
        That's why it's a usual practice to call the reset method at the end of
        the `getProduct` method body. However, this behavior is not mandatory,
        and you can make your builders wait for an explicit reset call from the
        client code before disposing of the previous result.
        """
        product = self._product
        self.reset()
        return product

    def produce_engine(self) -> None:
        self._product.add("1.5 dci")

    def produce_chassis(self) -> None:
        self._product.add("B0")

    def produce_coach(self) -> None:
        self._product.add("Sedan", "coach")


class Skoda(CarBuilder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """

    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """
        self.reset()

    def reset(self) -> None:
        self._product = Octavia()

    @property
    def product(self) -> Octavia:
        product = self._product
        self.reset()
        return product

    def produce_engine(self) -> None:
        self._product.add("1.9 tdi")

    def produce_chassis(self) -> None:
        self._product.add("PQ34")

    def produce_coach(self) -> None:
        self._product.add("Break")


class Automobil(ABC):
    def __init__(self):
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}")


class Logan(Automobil):
    """
    It makes sense to use the Builder pattern only when your products are quite
    complex and require extensive configuration.

    Unlike in other creational patterns, different concrete builders can produce
    unrelated products. In other words, results of various builders may not
    always follow the same interface.
    """

    def add(self, part: Any, part_type=None) -> None:
        if part_type == "coach":
            assert part.lower() in ("break", "sedan")
        self.parts.append(part)


class Octavia(Automobil):
    pass


class Director():
    def __init__(self, builder: CarBuilder):
        self.builder = builder

    def buildCar(self):
        self.builder.produce_chassis()
        self.builder.produce_engine()
        self.builder.produce_coach()
        return self.builder.product

    def changeBuilder(self, builder):
        self.builder = builder


if __name__ == "__main__":
    """
    The client code creates a builder object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder object.
    """
    dacia = Dacia()
    director = Director(dacia)
    car = director.buildCar()
    car.list_parts()

    director.changeBuilder(Skoda())
    new_car = director.buildCar()
    car.list_parts()
    new_car.list_parts()



# TODO Use the builder design patterns to build different types of houses
# (concrete house, wood house, container house, etc)
# All houses have a foundation, walls, roof and windows.
