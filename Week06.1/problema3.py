import functools

newlista = [21, 47, 33, 99, 62, 58, 48, 16, 15, 20, 81, 92, 10]

# lista2 = list(filter(lambda x: x % 2 == 0, lista))
# lista3 = list(map(lambda x: x*2, lista))
# result = functools.reduce(lambda x, y: x + y, lista)
# lista4 = list(zip(lista, [n % 2 for n in range(len(lista))]))

# # cum e cu map?

# # zip - compune perechi din mai multe liste
# l1 = [1, 2, 3, 4]
# l2 = [5, 6, 7, 8]
# l3 = zip(l1, l2)
# l3 = [(1, 5), (2, 6), (3, 7), (4, 8)]


# print(lista)
# print(lista2)
# print(lista3)
# print(lista4)


# lista2 = list(filter(lambda x: x % 2 == 0, lista))

# lista1  - elementele pare din lista noastra
# lista2  - lista cu cele impare
# lista3  - suma primelor doua elemente
# lista4  - 1 daca (lista1 + lista2) % 4 == 0 sau 0 daca nu este

lista1 = list(filter(lambda x: x % 2 == 0, newlista))
lista2 = list(filter(lambda x: x % 2 == 1, newlista))
# print(len(lista1))
# print(len(lista2))


def add_two_lists(listax, listay):
    listaz = []
    if len(listax) <= len(listay):
        for i in range(0, len(listax)):
            listaz.append(listax[i] + listay[i])
    else:
        for i in range(0, len(listay)):
            listaz.append(listax[i] + listay[i])
    return listaz


lista3 = add_two_lists(lista1, lista2)
print(lista3)


def elementul4(lista):
    listaz = []
    for i in range(len(lista)):
        if lista[i] % 4 == 0:
            listaz.append(1)
        else:
            listaz.append(0)
    return listaz


lista4 = elementul4(lista3)
print(lista4)

lista_provizorie = list(zip(list(filter(lambda x: x % 2 == 0, newlista)), list(
    filter(lambda x: x % 2 == 1, newlista)), lista3, lista4))


print(lista_provizorie)
