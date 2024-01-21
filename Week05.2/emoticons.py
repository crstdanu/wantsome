

user_input = "Buna dimineata! :)"


# metoda "split()" imparte un string in mai multe bucati
# in acest caz i-am spus sa imparta stringul atunci cand gaseste caracterul "spatiu gol"
# am vrut sa imi imparta propozitia in cuvinte(cuvintele in gramatica sunt despartite de spatiu)
# cuvintele vor fi salvate intr-o lista
lista_cuvinte = user_input.split(" ")

# print(lista_cuvinte)


dictionar_emoticoane = {
    ":)": "😄",
    ":(": "😔"
}



# creez variabila de tip "string" in care sa salvez rezultatul final
new_string = ""



# cu "for" iterez toate elementele din lista_cuvinte
# metoda "get()" la dictionare cauta un cuvant in dictionar si,
# daca il gaseste in dictionar, il inlocuieste cu valoarea lui
# daca nu il gaseste in dictionar il lasa asa cum e
# in cazul nostru, inlocuieste :) cu 😄, si atat
for item in lista_cuvinte:
    new_string += dictionar_emoticoane.get(item, item) + " "


print(new_string)

# fiecare poate sa adauge in dictionar cate elemente vrea
