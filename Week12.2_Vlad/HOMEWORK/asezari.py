class Tara:
    tari = []

    def __init__(self, nume: str):
        self.nume = nume
        self.__class__.tari.append(self)
        self.judete = []
        self.capitala = []

    def __str__(self):
        return self.nume

    def adauga_judet(self, judete):
        self.judete.append(judete)

    def adauga_capitala(self, judet):
        self.capitala.append(judet)

    def afiseaza_judetele(judete):
        if len(judete) > 0:
            for elem in judete:
                print(elem)
        else:
            print("Nu sunt judete inregistrate")


class Judet(Tara):
    comune = []
    orase = []

    def __init__(self, nume):
        self.nume = nume
        self.__class__.judete.append(self)
        self.orase = []
        self.comune = []

    def __str__(self):
        return self.nume

    def adauga_oras(self, oras):
        self.orase.append(oras)

    def adauga_comuna(self, comuna):
        self.comune.append(comuna)


class Oras(Judet):
    asezari = []

    def __init__(self, nume):
        self.nume = nume
        self.__class__.orase.append(self)
        self.cartiere = []

    def __str__(self):
        return self.nume

    def adauga_cartier(self, cartier):
        self.cartiere.append(cartier)


class Comuna(Judet):
    comune = []

    def __init__(self, nume):
        self.nume = nume
        self.__class__.comune.append(self)
        self.sate = []

    def __str__(self):
        return self.nume

    def adauga_sate(self, sat):
        self.sate.append(sat)


class Sat(Comuna):
    sate = []

    def __init__(self, nume):
        self.nume = nume
        self.__class__.sate.append(self)

    def __str__(self):
        return self.nume


romania = Tara("Romania")
iasi_judet = Judet("Iasi")
iasi_oras = Oras("Iasi")
miroslava = Comuna("Miroslava")
uricani = Sat("Uricani")
romania.adauga_judet("Iasi")
romania.adauga_judet("Vaslui")
romania.adauga_judet("Brasov")
romania.adauga_judet("Cluj-Napoca")
germania = Tara("Germania")
miroslava.adauga_sate("Uricani")

for obj in Tara.tari:
    print(obj)
