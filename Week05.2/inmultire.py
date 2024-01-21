
n = 5


lista = [[]]

for i in range(1, n+1):
    lista[0].append(i)

# lista = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]


for i in range(1, len(lista[0])):
    lista.append([])
    for x in range(len(lista[0])):
        lista[i].append(lista[0][x]*lista[0][i])


for item in lista:
    print(item)
