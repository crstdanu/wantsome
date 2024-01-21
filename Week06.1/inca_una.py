

newlista = [21, 47, 33, 99, 62, 58, 48, 16, 15, 20, 81, 92, 10]


lista1 = list(filter(lambda x: x % 2 == 0, newlista))
lista2 = list(filter(lambda x: x % 2 == 1, newlista))

lista3 = list((lista1[i] + lista2[i]
              for i in range(min(len(lista1), len(lista2)))))

# print(lista3)

lista4 = list((0 for i in lista3 if (i % 3 != 0))
              or (1 for i in lista3 if (i % 3 == 0)))

print(lista4)


def patru_conditii(lista):
    lista_noua = list(zip(list(filter(lambda x: x % 2 == 0, lista)), list(filter(lambda x: x % 2 == 1, lista)), list((list(filter(lambda x: x % 2 == 0, newlista))[i] + list(filter(lambda x: x % 2 == 1, newlista))[i] for i in range(min(len(list(filter(lambda x: x % 2 == 0, newlista))), len(list(filter(lambda x: x % 2 == 1, newlista))))))), list((0 for i in (list(
        filter(lambda x: x % 2 == 0, lista))[i] + list(filter(lambda x: x % 2 == 1, lista))[i] for i in range(len(list(filter(lambda x: x % 2 == 1, lista))))) if (i % 4 != 0)) or (1 for i in (list(filter(lambda x: x % 2 == 0, lista))[i] + list(filter(lambda x: x % 2 == 1, lista))[i] for i in range(len(list(filter(lambda x: x % 2 == 1, lista))))) if (i % 4 == 0)))))

    print(lista_noua)


# patru_conditii(newlista)
