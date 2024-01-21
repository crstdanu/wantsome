class Mediu:
    def __init__(self, nume):
        self.name = nume

    def __str__(self):
        return "Obiect:" + self.name


class Planta(Mediu):
    def __init__(self, nume):
        self.name = nume

    def __str__(self):
        return "Obiect:" + self.name


class Animal(Mediu):
    def __init__(self, nume):
        self.name = nume

    def __str__(self):
        return "Obiect:" + self.name


class Floare(Planta):
    def __init__(self, nume):
        self.name = nume

    def __str__(self):
        return "Obiect:" + self.name


class Pom(Planta):
    def __init__(self, nume):
        self.name = nume

    def __str__(self):
        return "Obiect:" + self.name


class Pasare(Animal):
    def __init__(self, nume):
        self.name = nume

    def __str__(self):
        return "Obiect:" + self.name


class Mamifer(Animal):
    def __init__(self, nume):
        self.name = nume

    def __str__(self):
        return "Obiect:" + self.name


mediu = Mediu("Padure")

f1 = Floare('Panseluta')
