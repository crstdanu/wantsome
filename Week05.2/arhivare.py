# input - AAAABBBAAACCCCCDAAB
# output - 4A3B3A5C1D2A1B

# - numarul de aparitii al urmatorrului caracter
# - caracterul respectiv

caractere = "AAAABBBAAACCCCCDAAB"

new_string = ""
litera = caractere[0]
numar_caractere = 1

for i in range(1, len(caractere)):
    if caractere[i] == litera:
        numar_caractere += 1
    else:
        new_string += str(numar_caractere) + litera
        litera = caractere[i]
        numar_caractere = 1

new_string += str(numar_caractere) + litera

print(new_string)
