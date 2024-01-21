def calculator_level2(string):
    lista_semne = []
    lista_numere = []
    numar = string[0]

    for i in string[1:]:
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


user = "4+9*(7-1+6*2)-11/(4-2)+3"
stripped_user = ""

# nu merge, nu e gata

while ("(" and ")") in user:
    x = user.index("(")
    y = user.index(")")
    felie = user[x+1:y]
    rezultat_felie = calculator_level2(felie)
    print(rezultat_felie)
    user = user.replace(f"({felie})", str(rezultat_felie))

print(user)
