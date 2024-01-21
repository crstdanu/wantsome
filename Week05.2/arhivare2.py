

text = "aaaabbbbcddwwwwwww"

arhiva = ""
litera_curenta = text[0]
count = 1


for item in text[1:]:
    if item == litera_curenta:
        count += 1
    else:
        arhiva += str(count) + litera_curenta
        litera_curenta = item
        count = 1

arhiva += str(count) + litera_curenta

print(arhiva)
