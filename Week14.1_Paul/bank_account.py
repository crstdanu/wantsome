

class CanaCafea:
    def __init__(self, volum, material):
        self.volum = volum
        self.material = material
        self.continut = 0

    def verificare_umplere(self, cantitate):
        if (self.volum - self.continut) >= cantitate:
            return
        else:
            raise Exception(
                f'Cana are doar {self.volum - self.continut} ml liberi')

    def verificare_golire(self, cantitate):
        if (self.continut - cantitate) > 0:
            return
        else:
            raise Exception(
                f'Cana are doar {self.continut} ml continut')

    def incarca_cana(self, cantitate):
        try:
            self.verificare_umplere(cantitate)
            self.continut += cantitate
        except Exception as error:
            print(f"Operatine nereusita: {error}")

    def goleste_cana(self, cantitate):
        try:
            self.verificare_golire(cantitate)
            self.continut -= cantitate
        except Exception as error:
            print(f"Operatine nereusita: Nu pot goli {cantitate} ml. {error}")

    def arata_continut(self):
        print(self.continut)


cana = CanaCafea(300, 'ceramica')

cana.incarca_cana(150)
cana.incarca_cana(250)
cana.arata_continut()
