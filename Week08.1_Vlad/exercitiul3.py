# generati un fisier json in care sa evm:
# 1. numarul de cuvinte
# 2. frecventele cuvintelor
# 3. lungimea celui mai lung cuvand + cuvantul
# 4. numarul total de consoane
# 5. numarul total de vocale

import re


def extrage_cuvintele(filename):

    lista_bruta = []
    with open(filename) as f:
        for linie in f.readlines():
            linie.strip()
            lista_bruta += re.split(r"[^A-Za-z]", string=linie)
    lista_cuvinte = [el for el in lista_bruta if el.isalpha()]

    dictionar_cuvinte = {}

    for item in lista_cuvinte:
        if item not in dictionar_cuvinte.keys():
            dictionar_cuvinte[item] = 1
        else:
            dictionar_cuvinte[item] += 1

    return dictionar_cuvinte


fisier = "Week8.1_Vlad/wiatrace.log"

rezultat = extrage_cuvintele(fisier)

rezultat_sortat = dict(sorted(rezultat.items(), key=lambda x: x[1]))
print(rezultat_sortat)
