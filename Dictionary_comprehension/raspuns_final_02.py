producatori = [
    {
        "nume": "Audi",
        "grup": "VAG",
        "tara": "Germania"
    },
    {
        "nume": "BMW",
        "grup": "BMW",
        "tara": "Germania"
    },
    {
        "nume": "Dacia",
        "grup": "Renault",
        "tara": "Romania"
    },
    {
        "nume": "Renault",
        "grup": "Renault",
        "tara": "Franta"
    },
    {
        "nume": "Volkswagen",
        "grup": "VAG",
        "tara": "Germania"
    },
]

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
        "producator": "Renaul",
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

# print(producatori[0])


def adauga_producatori(automobile, producatori):
    auto = [{key: (producatori[0] if value == "Audi" else producatori[1] if value == "BMW" else producatori[2] if value == "Dacia" else producatori[3]
                   if value == "Renault" else producatori[4] if value == "Volkswagen" else value) for (key, value) in automobile[i].items()} for i in range(len(automobile))]
    return auto


automobile_cu_producator = []

producatori_dict = {el['nume']: el for el in producatori}
# print(producatori_dict)


for masina in automobile:
    nume_prod = masina["producator"]
    masina["producator"] = producatori_dict.get(nume_prod)

print(automobile[2])


# for masina in automobile:
#     producator_masina = masina["producator"]
#     for producator in producatori:
#         if producator["nume"] == producator_masina:
#             masina["producator"] = producator
#         automobile_cu_producator.
