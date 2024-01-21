class Asezare:
    def __init__(self, nume, locuitori):
        self.nume = nume
        self.locuitori = locuitori

    def Afiseaza(self):
        pass

class Sat(Asezare):
    def __init__(self, nume, cod, locuitori):
        super().__init__(nume, locuitori)
        self.cod = cod

    def Afiseaza(self):
        print(f"nume = {self.nume}, locuitori = {self.locuitori}, cod = {self.cod}")

class Oras(Asezare):
    def __init__(self, nume, locuitori, este_resedinta):
        super().__init__(nume, locuitori)
        self.resedinta = este_resedinta

    def Afiseaza(self):
        print(f"nume = {self.nume}, locuitori = {self.locuitori}")

class Comuna(Asezare):
    def __init__(self, nume, locuitori):
        super().__init__(nume, locuitori)
        self.sate = []

    def Afiseaza(self):
        print(f"nume = {self.nume}, locuitori = {self.locuitori}")
        print('Sate:')
        for sat in self.sate:
            sat.Afiseaza()

    def AdaugaSat(self, sat):
        self.sate.append(sat)

class Judet(Asezare):
    def __init__(self, nume, locuitori, este_capitala):
        super().__init__(nume, locuitori)
        self.capitala = este_capitala
        self.orase = []
        self.comune = []

    def Afiseaza(self):
        print(f"nume = {self.nume}, locuitori = {self.locuitori}, capitala = {self.capitala}")
        print('Comune:')
        for comuna in self.comune:
            comuna.Afiseaza()
        print('Orase:')
        for oras in self.orase:
            oras.Afiseaza()
            
    def AdaugaOras(self, oras):
        self.orase.append(oras)

    def AdaugaComuna(self, comuna):
        self.comune.append(comuna)

class Tara(Asezare):
    def __init__(self, nume, locuitori):
        super().__init__(nume, locuitori)
        self.judete = []

    def Afiseaza(self):
        print(f"nume = {self.nume}, locuitori = {self.locuitori}")
        print("Judete:")
        for judet in self.judete:
            judet.Afiseaza()

    def AdaugaJudet(self, judet):
        self.judete.append(judet)    

s1 = Sat("Miroslava", 1, 100)
s2 = Sat("Valea Adanca", 2, 70)
s3 = Sat("Valea Ursului", 3, 90)
s4 = Sat("Ciurbesti", 4, 60)
s5 = Sat("Letcani", 5, 150)
s6 = Sat("Cucuteni", 6, 110)
c1 = Comuna("Miroslava", 400)
c2 = Comuna("Letcani", 300)
c1.AdaugaSat(s1)
c1.AdaugaSat(s2)
c1.AdaugaSat(s3)
c1.AdaugaSat(s4)

c2.AdaugaSat(s5)
c2.AdaugaSat(s6)

o1 = Oras("Iasi", 800000, True)
o2 = Oras("Pascani", 200000, False)
j1 = Judet("Iasi", 1000000, False)
j1.AdaugaOras(o1)
j1.AdaugaOras(o2)
j1.AdaugaComuna(c1)
j1.AdaugaComuna(c2)
o2 = Oras("Sector1", 5000000, False)
o3 = Oras("Bucuresti", 20000000, True)
j2 = Judet("Bucuresti", 20000000, True)
j2.AdaugaOras(o2)
j2.AdaugaOras(o3)
t1 = Tara("Romania", 30000000)
t1.AdaugaJudet(j1)
t1.AdaugaJudet(j2)

#t1.Afiseaza()
j2.Afiseaza()
