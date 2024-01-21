# Sa se afiseze histograma/frecventele fisierelor care au una din urmatoarele categorii de size
# ['G', 'M', 'K']  - [2**30, 2**20, 2**10]
# (100G, 50G), (50G, 10G), (10G, 5G), (5G, 1G), (1G, 100M)
# (100M, 50M), (50M, 10M), (10M, 5M), (5M, 1M), (1M, 100K)
# (100k, 50k), (50k, 10k), (10k, 5k), (5k, 1k), (1k, 100)
# --------------------------------------------------------------
# - fiecare categorie are specific numarul de fisiere si cat ocupa acestea in total {'50M-10M': [145, 12*(2**30)]}
#   - 145 - numarul de fisiere
#   - 12G - total cat ocupa
# informatiile despre fisere, aferente categoriilor de size se vor lista intr-un fiser pe linii separate sau intr-un format de bar-graph/chart
import os
import sys


fisiere = {}


def scaneaza(start_folder):
    for el in os.listdir(start_folder):
        path_full = os.path.join(start_folder, el)
        if os.path.isfile(path_full):
            size = os.path.getsize(path_full)
            fisiere[path_full] = size
        else:
            scaneaza(path_full)


folder = "C:\Program Files"

scaneaza(folder)


lista_chei = ["50G+", "50G-10G", "10G-5G", "5G-1G", "1G-100M", "100M-50M",
              "50M-10M", "10M-5M", "5M-1M", "1M-100K", "100K=50K", "50k-10K", "10K-5K", "5K-1K"]

dictionar_final = {}

for elem in lista_chei:
    dictionar_final[elem] = []

# for key, value in dictionar_final.items():
#     print(f"{key}: {value}")


for value in fisiere.values():
    if value > (50*2**30):
        if len(dictionar_final["50G+"]) < 2:
            dictionar_final["50G+"].append(1)
            dictionar_final["50G+"].append(value)
        else:
            dictionar_final["50G+"][0] += 1
            dictionar_final["50G+"][1] += value
    elif (value < (50*2**30)) and (value >= (10*2**30)):
        if len(dictionar_final["50G-10G"]) < 2:
            dictionar_final["50G-10G"].append(1)
            dictionar_final["50G-10G"].append(value)
        else:
            dictionar_final["50G-10G"][0] += 1
            dictionar_final["50G-10G"][1] += value
    elif (value < (10*2**30)) and (value >= (5*2**30)):
        if len(dictionar_final["10G-5G"]) < 2:
            dictionar_final["10G-5G"].append(1)
            dictionar_final["10G-5G"].append(value)
        else:
            dictionar_final["10G-5G"][0] += 1
            dictionar_final["10G-5G"][1] += value
    elif (value < (5*2**30)) and (value >= (1*2**30)):
        if len(dictionar_final["5G-1G"]) < 2:
            dictionar_final["5G-1G"].append(1)
            dictionar_final["5G-1G"].append(value)
        else:
            dictionar_final["5G-1G"][0] += 1
            dictionar_final["5G-1G"][1] += value
    elif (value < (1*2**30)) and (value >= (100*2**20)):
        if len(dictionar_final["1G-100M"]) < 2:
            dictionar_final["1G-100M"].append(1)
            dictionar_final["1G-100M"].append(value)
        else:
            dictionar_final["1G-100M"][0] += 1
            dictionar_final["1G-100M"][1] += value
    elif (value < (100*2**20)) and (value >= (50*2**20)):
        if len(dictionar_final["100M-50M"]) < 2:
            dictionar_final["100M-50M"].append(1)
            dictionar_final["100M-50M"].append(value)
        else:
            dictionar_final["100M-50M"][0] += 1
            dictionar_final["100M-50M"][1] += value
    elif (value < (50*2**20)) and (value >= (10*2**20)):
        if len(dictionar_final["50M-10M"]) < 2:
            dictionar_final["50M-10M"].append(1)
            dictionar_final["50M-10M"].append(value)
        else:
            dictionar_final["50M-10M"][0] += 1
            dictionar_final["50M-10M"][1] += value
    elif (value < (10*2**20)) and (value >= (5*2**20)):
        if len(dictionar_final["10M-5M"]) < 2:
            dictionar_final["10M-5M"].append(1)
            dictionar_final["10M-5M"].append(value)
        else:
            dictionar_final["10M-5M"][0] += 1
            dictionar_final["10M-5M"][1] += value
    elif (value < (5*2**20)) and (value >= (1*2**20)):
        if len(dictionar_final["5M-1M"]) < 2:
            dictionar_final["5M-1M"].append(1)
            dictionar_final["5M-1M"].append(value)
        else:
            dictionar_final["5M-1M"][0] += 1
            dictionar_final["5M-1M"][1] += value
    elif (value < (1*2**20)) and (value >= (100*2**10)):
        if len(dictionar_final["1M-100K"]) < 2:
            dictionar_final["1M-100K"].append(1)
            dictionar_final["1M-100K"].append(value)
        else:
            dictionar_final["1M-100K"][0] += 1
            dictionar_final["1M-100K"][1] += value
    elif (value < (100*2**10)) and (value >= (50*2**10)):
        if len(dictionar_final["100K=50K"]) < 2:
            dictionar_final["100K=50K"].append(1)
            dictionar_final["100K=50K"].append(value)
        else:
            dictionar_final["100K=50K"][0] += 1
            dictionar_final["100K=50K"][1] += value
    elif (value < (50*2**10)) and (value >= (10*2**10)):
        if len(dictionar_final["50k-10K"]) < 2:
            dictionar_final["50k-10K"].append(1)
            dictionar_final["50k-10K"].append(value)
        else:
            dictionar_final["50k-10K"][0] += 1
            dictionar_final["50k-10K"][1] += value
    elif (value < (10*2**10)) and (value >= (5*2**10)):
        if len(dictionar_final["10K-5K"]) < 2:
            dictionar_final["10K-5K"].append(1)
            dictionar_final["10K-5K"].append(value)
        else:
            dictionar_final["10K-5K"][0] += 1
            dictionar_final["10K-5K"][1] += value
    else:
        if len(dictionar_final["5K-1K"]) < 2:
            dictionar_final["5K-1K"].append(1)
            dictionar_final["5K-1K"].append(value)
        else:
            dictionar_final["5K-1K"][0] += 1
            dictionar_final["5K-1K"][1] += value


for key, value in dictionar_final.items():
    print(f"{key}: {value}")


# verificam correctitudinea operatiilor:

print(len(fisiere))

nr_fisiere = 0
for key in dictionar_final.keys():
    if len(dictionar_final[key]) > 0:
        nr_fisiere += dictionar_final[key][0]


if len(fisiere) == nr_fisiere:
    print("SUCCES")

# for key in fisiere.keys():
#     for elem in lista_chei:
#         if fisiere[key] > (50*2**30):
#             dictionar_final[elem] = []
