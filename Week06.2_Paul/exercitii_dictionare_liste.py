# Exercitii cu dictionare si liste
# Se dau urmatoarele liste de dictionare
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

# 1. Genereaza o lista extinsa de automobile, care sa contina elementele din automobile "expandate",
# folosind toate combinatiile de optiuni pentru motor si combustibil, fiecare element avand exact una dintre ele.
# Exemplu:
# {
#     "nume": "A3",
#     "producator": "Audi",
#     "an_fabricatie": "2010",
#     "motor": 2.0,
#     "optiuni_combustibil": "motorina"
# }

automobile_expandate = []

for x in automobile:
    for y, z in automobile[x].items():
        for z in automobile[x]["optiuni_combustibil"]:
            automobile_expandate.append(automobile[x][y:z])


# 2. Parcurge lista (originala) de automobile si adauga informatiile despre producator la fiecare model
# Exemplu:
# {
#     "nume": "A3",
#     "producator": {
#         "nume": "Audi",
#         "grup": "VAG",
#         "tara": "Germania"
#     },
#     "an_fabricatie": "2010",
#     "optiuni_motor": [1.4, 1.6, 1.8, 2.0],
#     "optiuni_combustibil": ["motorina", "benzina"]
# }

# 3. Printeaza automobilele in ordinea crescatoare a anului de fabricatie

# 4. Printeaza automobilul cu cele mai multe optiuni posibile (motor X combustibil)

# 5. Grupeaza automobilele dupa grupul producatorului intr-un nou dictionar.
# Exemplu
# {
#     "BMW": [
#         {
#             "nume": "Seria 3",
#             "producator": "BMW",
#             "an_fabricatie": "2005",
#             "optiuni_motor": [1.6, 2.0, 2.9, 3.0, 3.2],
#             "optiuni_combustibil": ["motorina", "benzina"]
#         },
#         {
#             "nume": "Seria 5",
#             "producator": "BMW",
#             "an_fabricatie": "2016",
#             "optiuni_motor": [1.6, 2.0, 3.0, 4.4],
#             "optiuni_combustibil": ["motorina", "benzina"]
#         }
#     ]
# }

# 6. Grupeaza automobilele dupa motor, combustibil:
# Exemplu
# {
#     "1.0_gpl": ["Dacia Logan 2024"]
# }

# 7. Afiseaza producatorul cu cele mai multe automobile, cat si numele acestora

# 8. Afiseaza grupul cu cele mai multe automobile mai noi de 10 ani

# BONUS: Pentru fiecare exercitiu de mai sus,
# creeaza o functie care returneaza rezultatul asteptat.

# 9. Creeaza o functie care creeaza varianta electrica pentru fiecare automobil si o adauga la lista de automobile
# Exemplu de automobil electric
# {
#     "nume": "Clio",
#     "producator": "Renault",
#     "an_fabricatie": "2025",  # aleator intre 2023 si 2030
#     "optiuni_motor": [0.0],
#     "optiuni_combustibil": ["electric"]
# }

# 10. Creeaza o functie ce returneaza lista de automobile filtrate dupa an de fabricatie, combustibil sau motor
# Toti parametri functiei sunt optionali.
