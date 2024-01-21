

lista = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
]

for i in range(1, len(lista[0])):
    lista.append([])
    lista[i].append(lista[0][0] * lista[0][i])
    for x in range(1, len(lista[0])):
        lista[i].append(lista[i][0] * lista[0][x])


for item in lista:
    print(item)
