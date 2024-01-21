# Genereaza o lista extinsa de automobile, care sa contina elementele din automobile "expandate",
# folosind toate combinatiile de optiuni pentru motor si combustibil, fiecare element avand exact una dintre ele.


auto = [
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
    for z in range(len(auto)):
        for i in range(len(auto[z]["optiuni_motor"])):
            for x in range(len(auto[z]["optiuni_combustibil"])):
                output += [{(key if key != "optiuni_motor" else "motor"): (auto[z]["nume"] if key == "nume" else auto[z]["producator"] if key == "producator" else auto[z]["an_fabricatie"] if key ==
                                                                           "an_fabricatie" else auto[z]["optiuni_combustibil"][x] if key == "optiuni_combustibil" else auto[z]["optiuni_motor"][i]) for key in auto[z]}]
    return output


# print(output[60])


# [{key: None for key in list}]
def expandat_2(lista_dict):
    inca_o_lista = []
    for el in lista_dict:
        for motor in el["optiuni_motor"]:
            for comb in el["optiuni_combustibil"]:
                copie = el.copy()
                copie.pop("optiuni_motor")
                copie.pop("optiuni_combustibil")
                copie["motor"] = motor
                copie["combustibil"] = comb
                inca_o_lista.append(copie)
    return inca_o_lista


lista_expandata = expandat_2(auto)
print(lista_expandata[53])
