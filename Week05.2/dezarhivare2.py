
text = "4a4b1c2d7w"

text_dezarhivat = ""

for item in range(0, len(text), 2):
    text_dezarhivat += int(text[item]) * text[item+1]

print(text_dezarhivat)

# cifre_litere = ""

# for item in text:
#     if item.isnumeric() == True:
#         cifre_litere += item
#     else:
#         cifre_litere += item + " "

# print(cifre_litere)

# lista_caractere = cifre_litere.split(" ")

# print(lista_caractere)
