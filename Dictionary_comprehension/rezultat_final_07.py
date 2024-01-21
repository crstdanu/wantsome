# Afiseaza producatorul cu cele mai multe automobile, cat si numele acestora

automobile = [
    {
        "nume": "A3",
        "producator": "Audi",
        "an_fabricatie": "2010",
        "optiuni_motor": [1.4, 1.6, 1.8, 2.0],
        "optiuni_combustibil": ["motorina", "benzina"]
    },
    {
        "nume": "A5",
        "producator": "Audi",
        "an_fabricatie": "2014",
        "optiuni_motor": [1.8, 2.0, 2.7, 3.0, 3.2],
        "optiuni_combustibil": ["motorina", "benzina"]
    },
    {
        "nume": "Seria 3",
        "producator": "BMW",
        "an_fabricatie": "2005",
        "optiuni_motor": [1.6, 2.0, 2.9, 3.0, 3.2],
        "optiuni_combustibil": ["motorina", "benzina"]
    },
    {
        "nume": "Seria 5",
        "producator": "BMW",
        "an_fabricatie": "2016",
        "optiuni_motor": [1.6, 2.0, 3.0, 4.4],
        "optiuni_combustibil": ["motorina", "benzina"]
    },
    {
        "nume": "Logan",
        "producator": "Dacia",
        "an_fabricatie": "2004",
        "optiuni_motor": [1.0, 1.2, 1.4, 1.5, 1.6],
        "optiuni_combustibil": ["motorina", "benzina", "gpl"]
    },
    {
        "nume": "Logan",
        "producator": "Dacia",
        "an_fabricatie": "2024",
        "optiuni_motor": [1.0, 1.2, 1.4, 1.6],
        "optiuni_combustibil": ["benzina", "gpl"]
    },
    {
        "nume": "Duster",
        "producator": "Dacia",
        "an_fabricatie": "2010",
        "optiuni_motor": [1.2, 1.4, 1.5, 1.6, 2.0],
        "optiuni_combustibil": ["motorina", "benzina"]
    },
    {
        "nume": "Clio",
        "producator": "Renault",
        "an_fabricatie": "2012",
        "optiuni_motor": [0.9, 1.2, 1.5, 1.6],
        "optiuni_combustibil": ["motorina", "benzina"]
    },
    {
        "nume": "Golf",
        "producator": "Volkswagen",
        "an_fabricatie": "1997",
        "optiuni_motor": [1.6, 1.8, 2.0, 2.8, 3.0, 3.2],
        "optiuni_combustibil": ["motorina", "benzina"]
    },
    {
        "nume": "Passat",
        "producator": "Volkswagen",
        "an_fabricatie": "2005",
        "optiuni_motor": [1.4, 1.6, 1.8, 1.9, 2.0, 2.8, 3.0, 3.6],
        "optiuni_combustibil": ["motorina", "benzina"]
    }
]

producatori = {}


for masina in automobile:
    for x in range(len(masina["optiuni_motor"])):
        for y in range(len(masina["optiuni_combustibil"])):
            if masina["producator"] not in producatori.keys():
                producatori[masina["producator"]] = []
                producatori[masina["producator"]] += [
                    f"{masina['producator']} {masina['nume']} {masina['an_fabricatie']} {masina['optiuni_motor'][x]} {masina['optiuni_combustibil'][y]}"]
            else:
                producatori[masina["producator"]
                            ] += [f'{masina["producator"]} {masina["nume"]} {masina["an_fabricatie"]} {masina["optiuni_motor"][x]} {masina["optiuni_combustibil"][y]}']


# for key, val in producatori.items():
#     print(f"{key}: {val}")

# print(len(producatori["Audi"]))

producatori_sortat = sorted(
    producatori, key=lambda x: len(producatori[x]), reverse=True)

# print(producatori_sortat)

producatori_sortat_2 = sorted(
    producatori.items(), key=lambda item: len(item[1]), reverse=True)

# for elem in producatori.items():
#     print(elem)

print(producatori_sortat_2)

# for x in producatori:
#     print(len(producatori[x]))


# print(len(producatori[producatori_sortat[0]]))

# lista_producatori = [{key: value} for (key, value) in producatori.items()]


# for x in lista_producatori:
#     print(x)


# lista_produccatori_sortata = sorted(
#     lista_producatori, key=lambda x: len(list(x.values())[0]), reverse=True)


# print(
#     f"Acesta este proucatorul impreuna cu lista de automobile: \n{lista_produccatori_sortata[0]}")


# dictionar = {
#     "Audi": [1, 2, 3],
#     "BMW": [a, a, a]
# }
