user_defined = "-1+9-71+1401"


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

print(lista_semne)
print(lista_numere)
print(numar)

rezultat = lista_numere[0]

for i in range(len(lista_semne)):
    rezultat += lista_numere[i+1] * \
        (-1) if lista_semne[i] == "-" else lista_numere[i+1]

print(rezultat)
