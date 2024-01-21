# Tema clase:
# In exercitiul cu Vehicule, se adauga o clasa numita Producator, cu nume, tara de origine si inventar (lista).
# Fiecare vehicul va avea un producator, iar vehiculele se pot crea doar printr-o metoda a producatorului (creeaza_vehicul).
# Producatorul va tine un inventar al automobilelor produse.
from culoare import Auto


class Producer:
    def __init__(self, name: str, country: str):
        self.name = name
        self.country = country
        self.inventory = []
        self.fuel_options = []
        self.engine_options = []

    def creeaza_vehicul(self, name, colour: str, fuel, engine):
        vehicle = Auto(name, self.name, colour, fuel, engine)
        assert fuel in self.fuel_options, f"Possible fuel options: {self.fuel_options}"
        assert engine in self.engine_options, f"Possible fuel options: {self.engine_options}"
        self.inventory.append(vehicle)
        return vehicle

    def add_fuel_options(self, option: str):
        assert option.lower() in ['gas', 'diesel', 'electric', 'gpl',
                                  ], "Possible fuel options: 'gas', 'diesel', 'electric', 'GPL'"
        self.fuel_options.append(option)
        # print("Fuel option added")

    def add_engine_options(self, option: float):
        assert option in [0.9, 1.0, 1.2, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9,
                          2.0], "Possible engine options: 0.9, 1.0, 1.2, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0"
        self.engine_options.append(option)
        # print("Engine option added")


vw = Producer("Volkswagen", "Germany")

# print(vw.country)
vw.add_fuel_options('electric')
vw.add_fuel_options('diesel')
vw.add_fuel_options('GPL')
vw.add_engine_options(1.0)
vw.add_engine_options(1.2)
vw.add_engine_options(1.4)
# print(vw.fuel_options)
# print(vw.engine_options)
passat = vw.creeaza_vehicul("Passat", "alb", 'diesel', 1.0)
print(passat.colour)
print(passat.engine)
print(passat.fuel)
print(passat.producator)
print(passat.name)
