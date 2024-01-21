# 10. Creeaza o functie ce returneaza lista de automobile FILTRATE dupa an de fabricatie, combustibil sau motor

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


def expandat(auto):
    output = []
    for elem in range(len(auto)):
        for motor in range(len(auto[elem]["optiuni_motor"])):
            for combustibil in range(len(auto[elem]["optiuni_combustibil"])):
                output += [{(key if key != "optiuni_motor" else "motor"): (auto[elem]["nume"] if key == "nume" else auto[elem]["producator"] if key == "producator" else auto[elem]["an_fabricatie"] if key ==
                                                                           "an_fabricatie" else auto[elem]["optiuni_combustibil"][combustibil] if key == "optiuni_combustibil" else str(auto[elem]["optiuni_motor"][motor])) for key in auto[elem]}]
    return output


auto_extinse = expandat(automobile)
# Creeaza o functie ce returneaza lista de automobile filtrate dupa an de fabricatie, combustibil sau motor


def filtreaza(input, lista_dictionare):
    def my_function(elem):
        # print(dict(elem).values())
        if input in dict(elem).values():
            return True
        else:
            return False

    new_list = list(filter(my_function, lista_dictionare))
    for item in new_list:
        print(item)


filtreaza("benzina", auto_extinse)
