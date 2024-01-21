# 3. Download the list of postcodes in Romania:
# https://data.gov.ro/datastore/dump/05359691-964d-4f82-87d7-bce1df66812e?bom=True
# Create a script that takes as an input a post code and prints the town/village name
# using data from the downloaded file.

# python postcode_translator.py 557095
# # Output: Gura Râului, SIBIU

import requests
import argparse


cod_postal = '617033'
url = "https://data.gov.ro/datastore/dump/05359691-964d-4f82-87d7-bce1df66812e?bom=True"
raspuns = requests.get(url)
continut_string = raspuns.content.decode('utf-8')


def afiseaza_localitatea(cod, continut):
    for linie in continut.splitlines():
        if str(cod) in linie:
            lista_linie = linie.split(",")
            print(f'\nOutput: {lista_linie[1]}, {lista_linie[2]}')
            break
    else:
        print("Code not found")


# afiseaza_localitatea(cod_postal)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A simple postal code finder')
    parser.add_argument('--postal_code', '-pc', type=int,
                        help='The postal code you want to find, as a 6 digits integer')
    args = parser.parse_args()
    postal_code = args.postal_code

    afiseaza_localitatea(postal_code, continut_string)
