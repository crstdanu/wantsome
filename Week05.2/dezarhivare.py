# "4A3B3A5C1D2A1B"

caractere = "4A3B3A5C1D2A1B"

new_string = ""
litera = caractere[1]
deinmultit = caractere[0]


for i in range(0, len(caractere), 2):
    deinmultit = caractere[i]
    litera = caractere[i+1]
    new_string += litera * int(deinmultit)

print(new_string)
