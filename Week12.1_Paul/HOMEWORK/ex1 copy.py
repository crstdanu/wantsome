# Ex 1
# Creeaza o functie ce primeste ca parametrul calea catre un director in sistemul de operare
# si organizeaza toate fisierele in directoare pe zile (se grupeaza fisierele dupa data crearii,
# se creeaza un director pentru fiecare data (cu formatul 2023-11-27) iar fisierele corespunzatoare
# sunt mutate in directorul respectiv.
# In fiecare director creat se creaza un fisier numit "metadata.json" care contine urmatoarele informatii:
# {
#     "nr_fisiere": 4,
#     "dimensiune_fisiere_mb": 12,
#     "cel_mai_mare_fisier": "image.jpg"
# }

import os
from datetime import datetime
import json


def organizeaza(cale):
    lista_fisiere = [os.path.join(cale, fisier) for fisier in os.listdir(
        cale) if os.path.isfile(os.path.join(cale, fisier))]

    for elem in lista_fisiere:
        timestamp_modificare = os.stat(elem).st_mtime
        obiect_timp = datetime.utcfromtimestamp(timestamp_modificare)
        data_modificare = obiect_timp.date().strftime('%Y_%m_%d')

        if data_modificare not in os.listdir(cale):
            os.mkdir(os.path.join(cale, data_modificare))

        noua_cale = os.path.join(os.path.join(
            cale, data_modificare), os.path.basename(elem))
        os.rename(elem, noua_cale)

    lista_directoare = os.listdir(cale)

    for director in lista_directoare:
        adresa = os.path.join(cale, director)

        metadata = {}
        nr_fisiere = 0
        dimensiune_fisiere_kb = 0
        cel_mai_mare_fisier = None

        for item in os.listdir(adresa):
            if os.path.isfile(os.path.join(adresa, item)):
                nr_fisiere += 1
                cale_fisier = os.path.join(adresa, item)
                dimensiune_fisiere_kb += (os.stat(cale_fisier).st_size) / (2**10)
                if os.stat(os.path.join(adresa, item)).st_size > os.stat(os.path.join(adresa, cel_mai_mare_fisier)).st_size:
                    cel_mai_mare_fisier = item

        metadata['nr_fisiere'] = nr_fisiere
        metadata['dimensiune_fisiere_kb'] = dimensiune_fisiere_kb
        metadata['cel_mai_mare_fisier'] = cel_mai_mare_fisier

        with open(f'{adresa}\metadata.json', 'w') as f:
            json.dump(metadata, f)


undeva = r"C:\Users\crstd\Desktop\Homework"

organizeaza(undeva)
