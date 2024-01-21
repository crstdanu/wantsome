
def calculator_level2(string):
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

    while True:
        if ("/" in lista_semne) and ("*" in lista_semne):
            if lista_semne.index("/") < lista_semne.index("*"):
                k = lista_semne.index("/")
                x = lista_numere[k] / lista_numere[k+1]
                del lista_numere[k:k+2]
                lista_numere.insert(k, x)
                del lista_semne[k]
                continue
            elif lista_semne.index("/") > lista_semne.index("*"):
                k = lista_semne.index("*")
                x = lista_numere[k] * lista_numere[k+1]
                del lista_numere[k:k+2]
                lista_numere.insert(k, x)
                del lista_semne[k]
                continue
        elif ("/" in lista_semne) and ("*" not in lista_semne):
            k = lista_semne.index("/")
            x = lista_numere[k] / lista_numere[k+1]
            del lista_numere[k:k+2]
            lista_numere.insert(k, x)
            del lista_semne[k]
            continue
        elif ("*" in lista_semne) and ("/" not in lista_semne):
            k = lista_semne.index("*")
            x = lista_numere[k] * lista_numere[k+1]
            del lista_numere[k:k+2]
            lista_numere.insert(k, x)
            del lista_semne[k]
            continue
        else:
            break

    rezultat = lista_numere[0]

    for i in range(len(lista_semne)):
        rezultat += lista_numere[i+1] * \
            (-1) if lista_semne[i] == "-" else lista_numere[i+1]

    return rezultat


user_defined = "-81/7*12+12*5/3-141/3"


print(round(calculator_level2(user_defined), 2))
