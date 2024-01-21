import re
from datetime import *
import argparse


def my_function(file):

    lista_chei = []
    lista_valori = []

    count = True
    with open(file) as f:
        for line in f.readlines():
            if count:
                lista_chei = line.strip().split(",")
                count = False
            else:
                lista_valori.append(line.strip().split(","))

    lista_dictionare = []

    for elem in lista_valori:
        dictionar = {}
        lista_dictionare.append(dictionar)
        for key, value in zip(lista_chei, elem):
            dictionar[key] = value

    for elem in lista_dictionare:
        elem["Date of birth"] = datetime.strptime(
            elem["Date of birth"], "%d.%m.%Y").date()
        elem["Score"] = int(elem["Score"])

    for elem in lista_dictionare:
        print(elem)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Insert the path to a CSV file')

    # Add positional argument
    parser.add_argument('file', type=str, help='The path')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the values using dot notation
    file = args.file

    my_function(file)
