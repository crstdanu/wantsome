conector = 'se gaseste in mediul'

class Mediu:
    def __init__(self, nume):
        self.mediu = nume

class Planta(Mediu):
    def __init__(self, mediu):
        super().__init__(mediu)
        self.tip = "Planta"

class Animal(Mediu):
    def __init__(self, mediu):
        super().__init__(mediu)
        self.tip = "Animalul"

class Floare(Planta):
    def __init__(self, nume, mediu):
        super().__init__(mediu)        
        self.nume = nume

    def __str__(self):
        return f"{self.tip} {self.nume} {conector} {self.mediu}"

class Leguma(Planta):
    def __init__(self, nume, mediu):
        super().__init__(mediu)
        self.nume = nume

    def __str__(self):
        return f"{self.tip} {self.nume} {conector} {self.mediu}"

class Copac(Planta):
    def __init__(self, nume, mediu):
        super().__init__(mediu)
        self.nume = nume

    def __str__(self):
        return f"{self.tip} {self.nume} {conector} {self.mediu}"

class Mamifer(Animal):
    def __init__(self, nume, mediu):
        super().__init__(mediu)
        self.nume = nume

    def __str__(self):
        return f"{self.tip} {self.nume} {conector} {self.mediu}"

class Pasare(Animal):
    def __init__(self, nume, mediu):
        super().__init__(mediu)
        self.nume = nume

    def __str__(self):
        return f"{self.tip} {self.nume} {conector} {self.mediu}"

elemente = [    
    Pasare('Papagal', 'Padure'), 
    Mamifer('Urs', 'Padure'), 
    Copac('Brad', 'Padure'), 
    Leguma('Cartof', 'Gradina'), 
    Floare('Lalea', 'Curte'),
    Mamifer('Caine', 'Curte'),
    Mamifer('Pisica', 'Curte'),
    Floare('Tei', 'Padure'),
    Pasare('Porumbel', 'Oras'),
    Leguma('Telina', 'Gradina'),
    Copac('Cires', 'Curte'),
    Copac('Cais', 'Curte')
]

for el in elemente:
    print(el)