from __future__ import annotations
from abc import ABC, abstractmethod


class TransportCreator(ABC):
    """
    The Creator class declares the factory method that is supposed to return an
    object of a Product class. The Creator's subclasses usually provide the
    implementation of this method.
    """

    @abstractmethod
    def create_transport(self):
        """
        Note that the Creator may also provide some default implementation of
        the factory method.
        """
        pass

    def transport(self) -> str:
        """
        Also note that, despite its name, the Creator's primary responsibility
        is not creating products. Usually, it contains some core business logic
        that relies on Product objects, returned by the factory method.
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of product from it.
        """

        # Call the factory method to create a Product object.
        product = self.create_transport()

        # Now, use the product.
        result = f"The packet has been shipped via {product.method_of_transportation()}"

        return result


"""
Concrete Creators override the factory method in order to change the resulting
product's type.
"""


class LandTransportCreator(TransportCreator):
    """
    Note that the signature of the method still uses the abstract product type,
    even though the concrete product is actually returned from the method. This
    way the Creator can stay independent of concrete product classes.
    """

    def create_transport(self) -> Product:
        return LandTransport()


class SeaTransportCreator(TransportCreator):
    def create_transport(self) -> Product:
        return SeaTransport()


class Product(ABC):
    """
    The Product interface declares the operations that all concrete products
    must implement.
    """

    @abstractmethod
    def method_of_transportation(self) -> str:
        pass

    @abstractmethod
    def km_per_day(self) -> int:
        pass

    @abstractmethod
    def cost_per_km(self) -> int:
        pass


"""
Concrete Products provide various implementations of the Product interface.
"""


class LandTransport(Product):
    def method_of_transportation(self) -> str:
        return "Truck"

    def km_per_day(self) -> int:
        return 500

    def cost_per_km(self) -> int:
        return 2


class SeaTransport(Product):
    def method_of_transportation(self) -> str:
        return "Ship"

    def km_per_day(self) -> int:
        return 250

    def cost_per_km(self) -> int:
        return 1


class AirTransport(Product):
    def method_of_transportation(self) -> str:
        return "Plane"

    def km_per_day(self) -> int:
        return 5000

    def cost_per_km(self) -> int:
        return 10


def ship_parcel(creator: TransportCreator, distance) -> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long as the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """
    print(f"The cost to send this parcel by {creator.transport}")


if __name__ == "__main__":
    print("App: Ship by land.")
    distance = 1000
    land_transport = LandTransportCreator()
    ship_parcel(land_transport, distance)
    print("\n")

    print("App: Ship by sea.")
    ship_parcel(SeaTransportCreator(), distance)
