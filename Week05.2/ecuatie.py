# ABCDE

lista = []

for a in range(0, 10):
    for b in range(0, 10):
        for d in range(0, 10):
            for e in range(0, 10):
                for c in range(0, 10):
                    if a + b == d - e:
                        element = str(a) + str(b) + str(c) + str(d) + str(e)
                        lista.append(element)


# for item in lista:
#     print(item)


# lista_numere = [int(i) for i in lista]

print(len(lista))
lista.sort()
# print(lista)


lista.sort(reverse=True)
# print(lista)
