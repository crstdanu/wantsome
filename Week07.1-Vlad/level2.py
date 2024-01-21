user_defined = "-81/7*12+12*5/3-141/3"


lista_semne = []
lista_numere = []
numar = user_defined[0]

for i in user_defined[1:]:
    if i.isnumeric():
        numar += i
    else:
        lista_semne += i
        lista_numere.append(int(numar))
        numar = ""
lista_numere.append(int(numar))


# print(lista_semne)
# print(lista_numere)


while True:
    if ("/" in lista_semne) and ("*" in lista_semne):
        if lista_semne.index("/") < lista_semne.index("*"):
            k = lista_semne.index("/")
            x = lista_numere[k] / lista_numere[k+1]
            # print(x)
            del lista_numere[k:k+2]
            lista_numere.insert(k, x)
            del lista_semne[k]
            # print(lista_semne)
            # print(lista_numere)
            continue
        elif lista_semne.index("/") > lista_semne.index("*"):
            k = lista_semne.index("*")
            x = lista_numere[k] * lista_numere[k+1]
            # print(x)
            del lista_numere[k:k+2]
            lista_numere.insert(k, x)
            del lista_semne[k]
            # print(lista_semne)
            # print(lista_numere)
            continue
    elif ("/" in lista_semne) and ("*" not in lista_semne):
        k = lista_semne.index("/")
        x = lista_numere[k] / lista_numere[k+1]
        # print(x)
        del lista_numere[k:k+2]
        lista_numere.insert(k, x)
        del lista_semne[k]
        # print(lista_semne)
        # print(lista_numere)
        continue
    elif ("*" in lista_semne) and ("/" not in lista_semne):
        k = lista_semne.index("*")
        x = lista_numere[k] * lista_numere[k+1]
        # print(x)
        del lista_numere[k:k+2]
        lista_numere.insert(k, x)
        del lista_semne[k]
        # print(lista_semne)
        # print(lista_numere)
        continue
    else:
        break


rezultat = lista_numere[0]

for i in range(len(lista_semne)):
    rezultat += lista_numere[i+1] * \
        (-1) if lista_semne[i] == "-" else lista_numere[i+1]

print(rezultat)


# for i in range(len(lista_semne)):
#     if (lista_semne[i] == "/") or (lista_semne[i] == "*"):
#         if lista_semne[i] == "/":
#             x = lista_numere[i] / lista_numere[i+1]
#             del lista_semne[i]
#             del lista_numere[i]
#             del lista_numere[i+i]
#             lista_numere.insert(i, x)
#             continue
#         else:
#             x = lista_numere[i] * lista_numere[i+1]
#             del lista_semne[i]
#             del lista_numere[i]
#             del lista_numere[i+i]
#             lista_numere.insert(i, x)
#             continue


# print(lista_semne)
# print(lista_numere)
