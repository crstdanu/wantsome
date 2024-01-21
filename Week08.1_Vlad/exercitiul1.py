# Generati o matrice de 10x10 sub forma unei liste de liste in care
# diagonala stanga_sus -> dreapta_jos sa aiba elemente 1, restul sa fie 0

def genereaza_matrice(latura=10):
    rezultat = []

    for i in range(latura):
        rezultat.append([])
        for x in range(latura):
            if i == x:
                rezultat[i].append("1")
            else:
                rezultat[i].append("0")

    return rezultat


rezultat = genereaza_matrice(5)

for elem in rezultat:
    print(elem)


def printeaza_frumos(rezultat: list):

    new_list = []
    for elem in rezultat:
        new_list.append("".join(elem))

    for elem in new_list:
        print(elem)


printeaza_frumos(rezultat)
