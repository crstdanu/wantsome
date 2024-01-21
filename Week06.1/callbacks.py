# unde le folosim?
# filter - pot sa filtrez elem unei liste dupa niste conditii (functii)
#
import functools

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista2 = list(filter(lambda x: x % 2 == 0, lista))
lista3 = list(map(lambda x: x*2, lista))
result = functools.reduce(lambda x, y: x + y, lista)
lista4 = list(zip(lista, [n % 2 for n in range(len(lista))]))

# cum e cu map?

# zip - compune perechi din mai multe liste
l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
l3 = zip(l1, l2)
l3 = [(1, 5), (2, 6), (3, 7), (4, 8)]


print(lista)
print(lista2)
print(lista3)
print(lista4)

newlista = [21, 47, 33, 99, 62, 58, 48, 16, 15, 20, 81, 92, 10]

lista2 = list(filter(lambda x: x % 2 == 0, lista))
