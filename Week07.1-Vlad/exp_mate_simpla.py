user_defined = "-1+4+9-5-6+4-2+8"

lista_numere = [int(x) for x in user_defined if x.isalnum()]

# print(lista_numere)

lista_semne = [x for x in user_defined if not x.isalnum()]
# print(lista_semne)


if len(lista_numere) != len(lista_semne):
    lista_semne = ["+"] + lista_semne

# print(lista_semne)

rezultat = 0

for i in range(len(lista_semne)):
    rezultat += lista_numere[i] * \
        (-1) if lista_semne[i] == "-" else lista_numere[i]

print(rezultat)
