import math


class Forma:
    def __init__(self, name):
        self.name = name


class Patrat(Forma):
    def __init__(self, latura):
        self.latura = latura

    def Arie(self):
        return self.latura**2

    def Perimetru(self):
        return self.latura*4

    def Nume(self):
        return self.name


class Cerc(Forma):
    def __init__(self, raza, x, y):
        self.raza = raza

    def Arie(self):
        return (self.raza ** 2) * math.pi

    def Perimetru(self):
        return 2*math.pi*self.raza

    def Nume(self):
        return self.name


class Dreptunghi(Forma):
    def __init__(self, lma, lmi):
        self.lmare = lma
        self.lmica = lmi

    def Arie(self):
        return self.lmare * self.lmica

    def Perimetru(self):
        return (2*self.lmare) + (2*self.lmica)

    def Nume(self):
        return self.name


class Triunghi(Forma):
    def __init__(self, la, lb, lc):
        self.la = la
        self.lb = lb
        self.lc = lc

    def _semiperimetru(self):
        return (self.la + self.lb + self.lc) // 2


patrat = Patrat(10)

print(patrat.Arie())
