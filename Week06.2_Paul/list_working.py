# automobile = [
#     {
#         "nume": "A3",
#         "producator": "Audi",
#         "an_fabricatie": "2010",
#         "optiuni_motor": [1.4, 1.6, 1.8, 2.0],
#         "optiuni_combustibil": ["motorina", "benzina"]
#     }]

# auto = [


# ]
# for x in automobile[0]["optiuni_motor"]:
#     auto += automobile[0]["optiuni_motor"]


lista1 = [[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]]

lista2 = []


for x in range(len(lista1)):
    for y in range(len(lista1[x])):
        for z in range(len(lista1[x][y])):
            lista2.append(lista1[x][y][z])

print(lista2)
# lista1[0][0][0]
# lista1[0][0][1]
# lista1[0][1][0]
# lista1[0][1][1]
# lista1[1][0][0]
# lista1[1][0][1]
# lista1[1][1][0]
# lista1[1][1][1]
# lista1[2][0][0]
# lista1[2][0][1]
# lista1[2][1][0]
# lista1[2][1][1]
