lista1_16 = [0x00, 0x00, 0xFC, 0x66, 0x66, 0x66, 0x7C,
             0x60, 0x60, 0x60, 0x60, 0xf0, 0x00, 0x00, 0x00, 0x00]

lista2_16 = [0x00, 0x00, 0x00, 0x00, 0x00, 0xC6, 0xC6,
             0xC6, 0xC6, 0xC6, 0xC6, 0x7E, 0x06, 0x0C, 0xF8, 0x00]

lista3_16 = [0x00, 0x00, 0x10, 0x30, 0x30, 0xFC, 0x30,
             0x30, 0x30, 0x30, 0x36, 0x1C, 0x00, 0x00, 0x00, 0x00]

lista4_16 = [0x00, 0x00, 0xE0, 0x60, 0x60, 0x6C, 0x76,
             0x66, 0x66, 0x66, 0x66, 0xE6, 0x00, 0x00, 0x00, 0x00]

lista5_16 = [0x00, 0x00, 0x00, 0x00, 0x00, 0x7C, 0xC6,
             0xC6, 0xC6, 0xC6, 0xC6, 0x7C, 0x00, 0x00, 0x00, 0x00]

lista6_16 = [0x00, 0x00, 0x00, 0x00, 0x00, 0xDC, 0x66,
             0x66, 0x66, 0x66, 0x66, 0x66, 0x00, 0x00, 0x00, 0x00]


lista1_02 = [bin(x) for x in lista1_16]
# print(lista1_02)

list1_02_fara_0b = [x[2:] for x in lista1_02]
print(list1_02_fara_0b)

lista2_02 = [bin(x) for x in lista2_16]
# print(lista2_02)
list2_02_fara_0b = [x[2:] for x in lista2_02]
# print(list2_02_fara_0b)

lista3_02 = [bin(x) for x in lista3_16]
# print(lista3_02)
list3_02_fara_0b = [x[2:] for x in lista3_02]
# print(list3_02_fara_0b)

lista4_02 = [bin(x) for x in lista4_16]
# print(lista4_02)
list4_02_fara_0b = [x[2:] for x in lista4_02]
# print(list4_02_fara_0b)

lista5_02 = [bin(x) for x in lista5_16]
# print(lista5_02)
list5_02_fara_0b = [x[2:] for x in lista5_02]
# print(list5_02_fara_0b)

lista6_02 = [bin(x) for x in lista6_16]
# print(lista6_02)
list6_02_fara_0b = [x[2:] for x in lista6_02]
# print(list6_02_fara_0b)

# decimal = [int(x) for x in list_02_fara_0b]
# print(decimal)


# final = [chr(x) for x in decimal]
# print(final)
# # lista_10 = [chr(x) for x in lista_02]

# print(lista_10)


def binary_to_string(bits):
    return ''.join([chr(int(i, 2)) for i in bits])


unu = binary_to_string(list1_02_fara_0b)
doi = binary_to_string(list2_02_fara_0b)
trei = binary_to_string(list3_02_fara_0b)
patru = binary_to_string(list4_02_fara_0b)
cinci = binary_to_string(list5_02_fara_0b)
sase = binary_to_string(list6_02_fara_0b)


for item in unu:
    print(item)
for item in doi:
    print(item)
for item in trei:
    print(item)
for item in patru:
    print(item)
for item in cinci:
    print(item)
for item in sase:
    print(item)
