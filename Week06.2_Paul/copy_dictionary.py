dictionar = {
    "nume": "A3",
    "producator": "Audi",
    "an_fabricatie": "2010",
    "optiuni_motor": [1.4, 1.6, 1.8, 2.0],
    "optiuni_combustibil": ["benzina", "motorina"]
}
lista_dictionare = []
print(len(dictionar["optiuni_combustibil"]))

copie_dictionar

for item in range(len(dictionar["optiuni_combustibil"])):
    lista_dictionare.append(dictionar.copy)
print(lista_dictionare)
# for x in range(len(dictionar["optiuni_combustibil"])):
#     lista_dictionare[x]["optiuni_combustibil"] = dictionar["optiuni_combustibil"][item]

# lista_dictionare[0]["optiuni_motor"] = dictionar["optiuni_motor"][0]
# lista_dictionare[0]["optiuni_combustibil"] = dictionar["optiuni_combustibil"][0]
# lista_dictionare[0]["optiuni_combustibil"] = dictionar["optiuni_combustibil"][1]

# lista_dictionare[1]["optiuni_motor"] = dictionar["optiuni_motor"][1]
# lista_dictionare[0]["optiuni_combustibil"] = dictionar["optiuni_combustibil"][0]
# lista_dictionare[0]["optiuni_combustibil"] = dictionar["optiuni_combustibil"][1]

# lista_dictionare[2]["optiuni_motor"] = dictionar["optiuni_motor"][2]
# lista_dictionare[3]["optiuni_motor"] = dictionar["optiuni_motor"][3]

print(lista_dictionare)
