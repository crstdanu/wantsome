from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Engine():
    def __init__(self, cc, comb, nr_cilindri):
        self.capacitate_cilindrica = cc
        self.combustibil = comb
        self.nr_cilindri = nr_cilindri

    def __str__(self):
        return f"Capacitate cilindrica: {self.capacitate_cilindrica}, Combustibil: {self.combustibil}, Cilindri: {self.nr_cilindri}"


class CarBuilder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    @property
    @abstractmethod
    def product(self) -> None:
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


class Automobil():
    def __init__(self) -> None:
        self.engine = None
        self.chassis = None
        self.coach = None
        self.optiuni = []

    def list_parts(self) -> None:
        print(
            f'Product parts: Motor: "{self.engine}", Sasiu: "{self.chassis}", Caroserie: "{self.coach}"')

    def add_optiune(self, optiune):
        self.optiuni.append(optiune)


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

    def produce_engine(self, cc, comb, nr_cilindri) -> Engine():
        motor = Engine(cc, comb, nr_cilindri)
        self._product.engine = motor
        return motor

    def produce_chassis(self) -> None:
        self._product.chassis = "B0"

    def produce_coach(self) -> None:
        self._product.coach = "Sedan"


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

    def produce_engine(self, cc, comb, nr_cilindri) -> Engine():
        motor = Engine(cc, comb, nr_cilindri)
        self._product.engine = motor
        return motor

    def produce_chassis(self) -> None:
        self._product.add("PQ34")

    def produce_coach(self) -> None:
        self._product.add("Break")


class Logan(Automobil):
    pass
    """
    It makes sense to use the Builder pattern only when your products are quite
    complex and require extensive configuration.

    Unlike in other creational patterns, different concrete builders can produce
    unrelated products. In other words, results of various builders may not
    always follow the same interface.
    """


class Octavia(Automobil):
    pass


if __name__ == "__main__":
    """
    The client code creates a builder object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder object.
    """
    dacia = Dacia()
    print("Custom product: ")
    dacia.produce_engine(1500, 'benzina', 4)
    dacia.produce_chassis()
    dacia.produce_coach()
    dacia.product.list_parts()
