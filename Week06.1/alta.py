

newlista = [21, 47, 33, 99, 62, 58, 48, 16, 15, 20, 81, 92, 10]


lista1 = list(filter(lambda x: x % 2 == 0, newlista))
lista2 = list(filter(lambda x: x % 2 == 1, newlista))
lista3 = list((lista1[i] + lista2[i] for i in range(len(lista2))if len(lista1) > len(lista2))
              or (lista1[i] + lista2[i] for i in range(len(lista1))if len(lista1) <= len(lista2)))

lista4 = list((0 for i in lista3 if (i % 4 != 0))
              or (1 for i in lista3 if (i % 4 == 0)))

# print(lista4)


lista_noua = list(zip(list(filter(lambda x: x % 2 == 0, newlista)), list(
    filter(lambda x: x % 2 == 1, newlista)), (list(filter(lambda x: x % 2 == 0, newlista))[i] + list(
        filter(lambda x: x % 2 == 1, newlista))[i] for i in range(len(list(
            filter(lambda x: x % 2 == 1, newlista))))), list((0 for i in (list(filter(lambda x: x % 2 == 0, newlista))[i] + list(
                filter(lambda x: x % 2 == 1, newlista))[i] for i in range(len(list(
                    filter(lambda x: x % 2 == 1, newlista))))) if (i % 4 != 0))
    or (1 for i in (list(filter(lambda x: x % 2 == 0, newlista))[i] + list(
        filter(lambda x: x % 2 == 1, newlista))[i] for i in range(len(list(
            filter(lambda x: x % 2 == 1, newlista))))) if (i % 4 == 0)))))


print(lista_noua)
