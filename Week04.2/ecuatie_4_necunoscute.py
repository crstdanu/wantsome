
# 4x + 2y - 6z + 2t = 0
# x - y + z + 4t = 20
# x - 2y + 5z - 3t = 3
# 5x + 10y + 10z + 5t = 70

lista_1 = []
lista_2 = []
lista_3 = []
lista_4 = []


for x in range(10):
    for y in range(10):
        for z in range(10):
            for t in range(10):
                if 4 * x + 2 * y - 6 * z + 2 * t == 0:
                    lista_1.append([x, y, z, t])


# for el in lista_1:
#     print(el)
# print(lista_1)

for x in range(10):
    for y in range(10):
        for z in range(10):
            for t in range(10):
                if x - y + z + 4 * t == 20:
                    lista_2.append([x, y, z, t])


for x in range(10):
    for y in range(10):
        for z in range(10):
            for t in range(10):
                if x - 2 * y + 5 * z - 3 * t == 3:
                    lista_3.append([x, y, z, t])


for x in range(10):
    for y in range(10):
        for z in range(10):
            for t in range(10):
                if 5 * x + 10 * y + 10 * z + 5 * t == 70:
                    lista_4.append([x, y, z, t])


rezultat = [
    el for el in lista_1 if el in lista_2 and el in lista_3 and el in lista_4]

print(rezultat)

# print(f"\nRezultatul este:\nX = {rezultat[0][0]}\nY = {rezultat[0][1]}\nZ = {rezultat[0][2]}\nT = {rezultat[0][3]}")
