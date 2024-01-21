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

lungime = 0
new_list = []

for i in range(len(automobile)):
    if len(automobile[i]["optiuni_motor"])*len(automobile[i]["optiuni_combustibil"]) > lungime:
        lungime = len(automobile[i]["optiuni_motor"]) * \
            len(automobile[i]["optiuni_combustibil"])
        new_list.append(automobile[i])

print(new_list[-1])
