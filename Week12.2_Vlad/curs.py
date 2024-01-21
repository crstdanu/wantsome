class Asezare:
    def __init__(self, name, ):
        self.name = name

    def afiseaza(self):
        print(self.name)


class Sat(Asezare):
    def __init__(self, name, cod, populatie):
        super().__init__(name)
        self.cod = cod
        self.populatie = populatie

    def afiseaza(self):
        print(self.nume, self.cod, self.populatie)


class Oras(Asezare):
    def __init__(self, name, locuitori):
        super().__init__(self, name, locuitori)


class Comuna(Asezare):
    def __init__(self, name, locuitori):
        super().__init__(name, locuitori)
