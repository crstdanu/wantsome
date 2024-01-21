
# Insering to a list methods

lista_float = [0.12, 0.13, 1.15]

lista_integer = [1, 3, 9, 11, 4, 56, 6]

lista_caractere = ["a", "q", "s", "v"]

lista_cuvinte = ["Vasile", "Gheorghe", "acasa", "mancare"]

##################################
# Transformari ale elementelor din lista
# la primul x aplicam transsformarea
# traducerea ar fi: pune in lista new_list cate un int(x) pentru fiecare element x din lista "lista"

new_list = [int(x) for x in lista_float]  # functia int() rotunjeste in jos
print(new_list)


####################################

# append()
# list.append(element)
# the elemet can be a string, integer, another list, etc.

lista_float.append(4.25)
print(lista_float)

# daca argumentul e o lista il adauga ca o lista intreaga, nu element cu element

lista_float.append(lista_integer)
print(lista_float)


#####################################
# FUNCTIONS FOR STRINGS ONLY
# join()

# join() transforma elementele unei liste intr-un STRING (o variabila de tip STRING)


list1 = ["c", "r", "i", "s", "t", "i", "a", "n",]

string1 = "".join(list1)
print(string1)
print(type(string1))  # lista2 nu e lista ci e o variabila de tip string

string3 = "-".join(list1)
print(string3)

# lista4 = "".join(lista_integer) --> NOT WORKING because the elements from lista_integer are NOT STRINGS

###############################################

# extend()
# used to extend a list with the elements os another list
# the difference between "append" and "extend" is theat append() sees a list as 1 (one) element but extend sees a list as a collection of elements

# lista_float.append(lista_integer) --> adauga intreaga lista_integer ca un element la lista_float
# lista_float.extend(lista_integer) --> adauga elementele din lista_integer la lista_float, element cu element

lista5 = []
lista_float.extend(lista_integer)
print(lista_float)


# cum adaug elemente intr-o lista?

# element cu element


# numere = [1, 2, 3]
# caractere = ["1", "2", "3"]


# print(caractere)
# print(type(caractere))


# caractere += "".join(lista_caractere[2:6])  # adauga element cu element

# print(caractere)
# print(type(caractere))


# # caractere.append(lista_caractere)  # ca sa completez lista "caractere" cu un singur element ce contine intreaga "lista_caractere"
# # ca sa completez lista "caractere" cu toatele elementele din "lista_caractere" unul cate unu.
# caractere.extend(lista_caractere)

# print(caractere)
