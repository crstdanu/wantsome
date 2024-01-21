# avion - gri, auriu
# auto - orice culoare
# barca - alb, albastru, rosie, gri, mov

class Vehicul:
    def __init__(self, producator: str):
        self.producator = producator


class Avion(Vehicul):
    def __init__(self, producator, colour: str):
        super().__init__(producator)

        assert colour.lower() in [
            'gri', 'auriu'], "Optiuni de culoare: 'gri' si 'auriu'"

        self.colour = colour


class Auto(Vehicul):
    def __init__(self, name, producator, colour: str, fuel, engine):
        super().__init__(producator)
        self.colour = colour
        self.fuel = fuel
        self.engine = engine
        self.name = name


class Barca(Vehicul):
    def __init__(self, producator, colour: str):
        super().__init__(producator)

        assert colour.lower() in ['alb', 'albastru', 'rosu', 'gri',
                                  'mov'], "Optiuni de culoare: 'alb', 'albastru', 'rosu', 'gri' si 'mov'"

        self.colour = colour


item1 = Avion("Cessna", "gri")
print(item1.colour)

# item2 = Auto("Dacia", "rosu")
# print(item2.colour)

item3 = Barca("Yamaha", "mov")
print(item3.colour)
