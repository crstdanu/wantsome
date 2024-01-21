import math
import random
import tkinter
import json

# clasa de baza cu proprietatile (x,y,nume) si metodele (Arie,Perimetru) comune


class Shape:
    def __init__(self, x, y, nume):
        self.x = x
        self.y = y
        self.nume = nume

    def Arie(self):
        pass

    def Perimetru(self):
        pass

# clasa Patrat care adauga l la un Shape numit 'Patrat' si redefineste cum arata Perimetru si Arie


class Patrat(Shape):
    def __init__(self, l, x, y):
        super().__init__(x, y, "Patrat")
        self.l = l

    def Arie(self):
        return self.l ** 2

    def Perimetru(self):
        return self.l * 4

    def __str__(self):
        return str('\"' + self.nume + '\"' + ': {\"l\":' + str(self.l) + ", \"x\": " + str(self.x) + ", \"y\": " + str(self.y) + '}')

# clasa Cerc care adauga r la un Shape numit 'Cerc' si redefineste cum arata Perimetru si Arie


class Cerc(Shape):
    def __init__(self, r, x, y):
        super().__init__(x, y, "Cerc")
        self.r = r

    def Arie(self):
        return (self.r ** 2) * math.pi

    def Perimetru(self):
        return 2 * math.pi * self.r

    def __str__(self):
        return str('\"' + self.nume + '\"' + ': {\"r\":' + str(self.r) + ", \"x\": " + str(self.x) + ", \"y\": " + str(self.y) + '}')

# clasa Dreptunghi care adauga lma (latura mare) si lmi (latura mica) la un Shape numit 'Dreptunghi' si redefineste cum arata Perimetru si Arie


class Dreptunghi(Shape):
    def __init__(self, lma, lmi, x, y):
        super().__init__(x, y, "Dreptunghi")
        self.lma = lma
        self.lmi = lmi

    def Arie(self):
        return self.lma * self.lmi

    def Perimetru(self):
        return sum([2 * self.lma, 2*self.lmi])

    def __str__(self):
        return str('\"' + self.nume + '\"' + ': {\"L\":' + str(self.lma) + ", \"l\":" + str(self.lmi) + ", \"x\": " + str(self.x) + ", \"y\": " + str(self.y) + '}')

# clasa Triunghi care adauga la (latura a), lb (latura b) si lc (latura c) la un Shape numit 'Triunghi' si redefineste cum arata Perimetru si Arie


class Triunghi(Shape):
    def __init__(self, la, lb, lc, x, y):
        super().__init__(x, y, "Triunghi")
        self.la = la
        self.lb = lb
        self.lc = lc

    def _semiperimetru(self):
        return (self.la + self.lb + self.lc) // 2

    def Arie(self):
        sm = self._semiperimetru()
        result1 = sm * (sm - self.la) * (sm - self.lb) * (sm - self.lc)
        # daca result1>0 atunci laturile formeaza un triunghi valid
        if result1 > 0:
            result2 = math.sqrt(result1)
        # daca rezultatul este negativ, atunci inseamna ca una din laturi este atat de mare incat celelalte 2 nu se mai intalnesc
        else:
            result2 = 0
        return result2

    def Perimetru(self):
        return sum([self.la, self.lb, self.lc])

    def __str__(self):
        return str('\"' + self.nume + '\"' + ': {\"la\":' + str(self.la) + ", \"lb\":" + str(self.lb) + ", \"lc\":" + str(self.lc) + ", \"x\": " + str(self.x) + ", \"y\": " + str(self.y) + '}')

# construim o forma aleatorie dintre Cerc, Patrat, Dreptunghi, Triunghi


def GenereazaForma():
    forme = [Patrat, Cerc, Dreptunghi, Triunghi]
    x = random.choice(range(10, 500))
    y = random.choice(range(10, 500))
    index_forma = random.choice(range(0, 4))
    # patratul si cercul au un singur parametru care este ori raza ori latura
    if index_forma < 2:
        p1 = random.choice(range(10, 200))
        return forme[index_forma](p1, x, y)
    # Dreptunghiul are 2 parametri - lmi, lma
    elif index_forma == 2:
        while True:
            p1 = random.choice(range(10, 200))
            p2 = random.choice(range(10, 200))
            if p1 > p2:
                return forme[index_forma](p1, p2, x, y)
    # Triunghiul are 3 parametri (la, lb, lc)
    elif index_forma == 3:
        # un triunghi este valid daca Aria acestuia nu este 0
        while True:
            p1 = random.choice(range(10, 200))
            p2 = random.choice(range(10, 200))
            p3 = random.choice(range(10, 200))
            triunghi_valid = forme[index_forma](p1, p2, p3, x, y)
            if triunghi_valid.Arie() > 0:
                return triunghi_valid


# forme = [GenereazaForma() for i in range(100)]
# for f in forme:
#     print(f"{f}, P: {f.Perimetru()}, A: {f.Arie()}")


def start_desen():
    forme = [GenereazaForma() for i in range(100)]
    forme = []
    for f in forme:
        # print(f"{f}, P: {f.Perimetru()}, A: {f.Arie()}")
        nume_forma = str(f).split(':')[0][1:-1]
        forme = {}
        forme[nume_forma] = {}


window = tkinter.Tk()
window.title("Forme geometrice")
window.geometry("600x600")

desen = tkinter.Canvas(window, width=550, height=550)
desen.grid(row=0, column=0)


tkinter.Button(text="Porneste", command=start_desen).grid(row=1, column=1)


window.mainloop()
