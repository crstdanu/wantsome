
user = "Hello python!"

# format()- This method takes a value and inserts it where the placeholders are present, it is also used to merge the parts of a string at specified intervals.

# The ord() function returns the number representing the unicode code of a specified character.


# lista_unicode = [ord(x) for x in user]

# print(lista_unicode)

# ord() transforma din orice string in numar zecimal
# hex() transfeorma din nr zecimal in hexadecimal(baza 16)

baza_16 = [hex(ord(x))[2:] for x in user]

print(baza_16)


baza_2 = [bin(ord(x))[2:] for x in user]
print(baza_2)


# list comprehension : [x for x in colectie]
