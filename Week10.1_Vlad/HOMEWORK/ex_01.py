# 1. Folosind un fisier text oarecare cu extensia .log,
# din sistemul vostru de operare, scrieti o expreise regulata care sa
# identifice toate propozitiile care contin exact 2 virgule.

# O propozitie incepe cu o litera mare si se termina cu punct.
# Exemplu:
# Am fost la mare, apoi am fost la munte, apoi am revenit acasa.


import os
import re

path = os.getcwd()

rezultate = []
exemplu = """
Am fost la mare, apoi am fost la munte, apoi am revenit acasa.
Folosind un fisier text oarecare cu extensia .log, din sistemul vostru de operare, scrieti o expreise regulata care sa identifice toate propozitiile care contin exact 2 virgule.
De cealaltă parte, șeful de la CNAIR spune că nici nu se va mai discuta de o descărcare temporară, ci speră ca anul viitor constructorul lotului adiacent - chinezii de la CCECC care au semnat contractul în primăvară - vor prioritiza și vor termina în timp record (n.r.) legătura și nodul rutier cu DN2.
"""
# pattern = re.compile(
#     r"([A-Z][a-z0-9]+)\,\s([A-Z][a-z0-9]+)\,\s([A-Z][a-z0-9]+)\.")

with open(f"{path}\Week10.1_Vlad\HOMEWORK\wiatrace.log") as f:
    for line in f.readlines():
        rez = re.findall(
            r"[A-Z][A-Za-z0-9\.?\s?]+\,\s[A-Za-z0-9\s?\.?]+\,\s[A-Za-z0-9\s?\.?]+\.", line)
        # rez = pattern.finditer(line)
        rezultate += rez


rezultate = list(set(rezultate))
for line in rezultate:
    print(line)
