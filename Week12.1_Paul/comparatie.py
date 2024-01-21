class Animal:
    metoda_de_deplasare = "se deplaseaza"

    def __init__(self, regn, specie, nume, este_periculos=False, habitat=None, greutate=None, **kwargs):
        self.regn = regn
        self.specie = specie
        self.habitat = habitat
        self.nume = nume
        self.este_periculos = este_periculos
        self.greutate = greutate
        self.atribute_extra = kwargs

    def deplaseaza(self):
        return f"{self} si {self.metoda_de_deplasare} pe {self.habitat}"

    def __str__(self):
        return f"{self.nume} este o {self.specie} din regnul {self.regn}"

    def __eq__(self, other):
        return self.greutate == other.greutate

    def __lt__(self, other):
        return self.greutate < other.greutate

    def __gt__(self, other):
        return self.greutate > other.greutate

    def __add__(self, other):
        return self.greutate + other.greutate


class AnimalDeUscat(Animal):
    metoda_de_deplasare = "merge"

    def __init__(self, regn=None, specie=None, nume=None, este_periculos=False, **kwargs):
        if "habitat" in kwargs:
            kwargs.pop("habitat")
        super().__init__(regn=regn, specie=specie, habitat="uscat", nume=nume,
                         este_periculos=este_periculos, **kwargs)


class AnimalZburator(AnimalDeUscat):
    def __init__(self, regn, specie, nume, este_periculos=False):
        nume += " Zboratorul"
        super().__init__(regn=regn, specie=specie, nume=nume, este_periculos=este_periculos)

    def deplaseaza(self):
        return f"{super().deplaseaza()} si zboara prin aer"


class AnimalDeApa(Animal):
    metoda_de_deplasare = "inoata"

    def __init__(self, regn, specie, nume, este_periculos=False, **kwargs):
        super().__init__(regn=regn, specie=specie, habitat="apa", nume=nume,
                         este_periculos=este_periculos, **kwargs)

    def deplaseaza(self):
        return f"{self} si {self.metoda_de_deplasare} prin {self.habitat}"


class Mamifer(Animal):
    metoda_de_reproducere = "naste pui"

    def __init__(self, specie=None, habitat=None, nume=None, este_periculos=False, **kwargs):
        super().__init__(regn="mamifer", specie=specie, habitat=habitat, nume=nume,
                         este_periculos=este_periculos, **kwargs)


class MamiferDeUscat(Mamifer, AnimalDeUscat):
    def __init__(self, specie, nume, este_periculos, **kwargs):
        super().__init__(specie=specie, nume=nume, este_periculos=este_periculos, **kwargs)


foxy = MamiferDeUscat(specie="vulpe", nume="Foxy", este_periculos=True, greutate=20)
willy = AnimalDeApa("mamifer", "balena", "Willy", greutate=2000)
animal3 = AnimalZburator("pasare", "rata", "Donald", False)


print(sorted([foxy, willy], reverse=True))

# Se defineste o clasa de baza numita Vehicul
# Apoi se definesc 3 subclase pentru aer/uscat/apa
# Se creeaza cate 2 obiecte pentru fiecare subclasa intr-o lista de vehicule
# Lista de vehicule se sorteaza tinand cont de viteza cu care circula

