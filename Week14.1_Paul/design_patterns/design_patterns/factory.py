from __future__ import annotations
from abc import ABC, abstractmethod
# design pattern - daca exista o metoda abstracta


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


class AirTransportCreator(TransportCreator):
    def create_transport(self) -> Product:
        return AirTransport()


class Product(ABC):
    """
    The Product interface declares the operations that all concrete products
    must implement.
    """

    @abstractmethod
    def method_of_transportation(self) -> str:
        pass

    def cost_transport(self) -> int:
        pass

    def durata_transport(self) -> int:
        pass


"""
Concrete Products provide various implementations of the Product interface.
"""


class LandTransport(Product):
    def __init__(self):
        self.price = 10
        self.speed = 45

    def method_of_transportation(self) -> str:
        return "Truck"

    def cost_transport(self, distanta):
        return self.price * distanta

    def durata_transport(self, distanta):
        return distanta / self.speed


class SeaTransport(Product):
    def __init__(self):
        self.price = 1
        self.speed = 5

    def method_of_transportation(self) -> str:
        return "Ship"

    def cost_transport(self, distanta):
        return self.price * distanta

    def durata_transport(self, distanta):
        return distanta / self.speed


class AirTransport(Product):
    def __init__(self):
        self.price = 100
        self.speed = 400

    def method_of_transportation(self) -> str:
        return "Air"

    def cost_transport(self, distanta):
        return self.price * distanta

    def durata_transport(self, distanta):
        return distanta / self.speed


def ship_parcel(creator: TransportCreator, distanta, timp=None, cost=None) -> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long as the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """
    transport = creator.create_transport()
    if timp and cost:
        return transport.cost_transport(distanta) * transport.durata_transport(distanta)
    elif timp:
        return transport.durata_transport(distanta)
    elif cost:
        return transport.cost_transport(distanta)
    else:
        return transport.cost_transport(distanta) * transport.durata_transport(distanta)

    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.transport()}", end="")


if __name__ == "__main__":

    distanta = 1000

    land = ship_parcel(LandTransportCreator(), distanta, cost=True)
    air = ship_parcel(AirTransportCreator(), distanta, cost=True)
    sea = ship_parcel(SeaTransportCreator(), distanta, cost=True)
    print(land)
    print(air)
    print(sea)
    print(min(land, air, sea))
