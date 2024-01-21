
def encripteaza(fisier, pas=3):

    f = open(fisier)
    date_fisier = f.read()
    new_lista = [chr(ord(letter)+pas) if letter.isalpha()
                 else letter for letter in date_fisier]
    new_data = "".join(new_lista)
    new_file_name = ".".join(fisier.split(
        ".")[:-1]) + "_criptat" + "." + fisier.split(".")[-1]
    with open(new_file_name, "w") as x:
        x.write(new_data)
    f.close()


encripteaza("Week6.2/altul.txt")

# chr(ord(letter)+pas) if letter.isalpha() for letter in date_fisier
