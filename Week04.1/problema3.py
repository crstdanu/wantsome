user_defined = "1+4+9-5-6+4-2+8"

lista = [int(x) for x in user_defined if x.isalnum()]

print(lista)

lista_semne = [x for x in user_defined if not x.isalnum()]
print(lista_semne)


if len(lista) != len(lista_semne):
    lista_semne = ["+"] + lista_semne

print(lista_semne)

var = 0

for i in range(len(lista_semne)):
    var += lista[i]*(-1) if lista_semne[i] == "-" else lista[i]

print(var)
