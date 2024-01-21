
import os


def scan_files(path):

    fisiere = {}

    def scaneaza(start_folder):
        for el in os.listdir(start_folder):
            path_full = os.path.join(start_folder, el)
            if os.path.isfile(path_full):
                size = os.path.getsize(path_full)
                fisiere[path_full] = size
            else:
                scaneaza(path_full)

    scaneaza(path)

    lista_chei = ["50G+", "50G-10G", "10G-5G", "5G-1G", "1G-100M", "100M-50M", "50M-10M",
                  "10M-5M", "5M-1M", "1M-100K", "100K=50K", "50k-10K", "10K-5K", "5KandLESS"]

    dictionar_final = {}

    for elem in lista_chei:
        dictionar_final[elem] = [0, 0]

    lista_valori_numerice = [(50*2**30, 10*2**30), (10*2**30, 5*2**30), (5*2**30, 1*2**30), (1*2**30, 100*2**20), (100*2**20, 50*2**20), (50*2**20, 10*2**20),
                             (10*2**20, 5*2**20), (5*2**20, 1*2**20), (1*2**20, 100*2**10), (100*2**10, 50*2**10), (50*2**10, 10*2**10), (10*2**10, 5*2**10)]

    for value in fisiere.values():
        if value > (50*2**30):
            dictionar_final["50G+"][0] += 1
            dictionar_final["50G+"][1] += value
        elif value < (5*2**10):
            dictionar_final["5KandLESS"][0] += 1
            dictionar_final["5KandLESS"][1] += value
        else:
            for i, elem in enumerate(lista_valori_numerice):
                if value < elem[0] and value > elem[1]:
                    dictionar_final[lista_chei[i+1]][0] += 1
                    dictionar_final[lista_chei[i+1]][1] += value
                    break

    # for value in fisiere.values():
    #     if value > (50*2**30):
    #         dictionar_final["50G+"][0] += 1
    #         dictionar_final["50G+"][1] += value
    #     elif (value < (50*2**30)) and (value >= (10*2**30)):
    #         dictionar_final["50G-10G"][0] += 1
    #         dictionar_final["50G-10G"][1] += value
    #     elif (value < (10*2**30)) and (value >= (5*2**30)):
    #         dictionar_final["10G-5G"][0] += 1
    #         dictionar_final["10G-5G"][1] += value
    #     elif (value < (5*2**30)) and (value >= (1*2**30)):
    #         dictionar_final["5G-1G"][0] += 1
    #         dictionar_final["5G-1G"][1] += value
    #     elif (value < (1*2**30)) and (value >= (100*2**20)):
    #         dictionar_final["1G-100M"][0] += 1
    #         dictionar_final["1G-100M"][1] += value
    #     elif (value < (100*2**20)) and (value >= (50*2**20)):
    #         dictionar_final["100M-50M"][0] += 1
    #         dictionar_final["100M-50M"][1] += value
    #     elif (value < (50*2**20)) and (value >= (10*2**20)):
    #         dictionar_final["50M-10M"][0] += 1
    #         dictionar_final["50M-10M"][1] += value
    #     elif (value < (10*2**20)) and (value >= (5*2**20)):
    #         dictionar_final["10M-5M"][0] += 1
    #         dictionar_final["10M-5M"][1] += value
    #     elif (value < (5*2**20)) and (value >= (1*2**20)):
    #         dictionar_final["5M-1M"][0] += 1
    #         dictionar_final["5M-1M"][1] += value
    #     elif (value < (1*2**20)) and (value >= (100*2**10)):
    #         dictionar_final["1M-100K"][0] += 1
    #         dictionar_final["1M-100K"][1] += value
    #     elif (value < (100*2**10)) and (value >= (50*2**10)):
    #         dictionar_final["100K=50K"][0] += 1
    #         dictionar_final["100K=50K"][1] += value
    #     elif (value < (50*2**10)) and (value >= (10*2**10)):
    #         dictionar_final["50k-10K"][0] += 1
    #         dictionar_final["50k-10K"][1] += value
    #     elif (value < (10*2**10)) and (value >= (5*2**10)):
    #         dictionar_final["10K-5K"][0] += 1
    #         dictionar_final["10K-5K"][1] += value
    #     else:
    #         dictionar_final["5KandLESS"][0] += 1
    #         dictionar_final["5KandLESS"][1] += value

    return dictionar_final


folder = "e:\Download"

valori_scan = scan_files(folder)
try:
    for key, value in valori_scan.items():
        print(f"{key}: {value}")
except:
    print(valori_scan)

# aflam maximul valorilor
maxim_1 = 0
for k, v in valori_scan.items():
    if valori_scan[k][1] > maxim_1:
        maxim_1 = valori_scan[k][1]

maxim_0 = 0
for k, v in valori_scan.items():
    if valori_scan[k][0] > maxim_0:
        maxim_0 = valori_scan[k][0]


max_k = 0
for k in valori_scan.keys():
    if len(k) > max_k:
        max_k = len(k)


# transformam in puncte procentuale
procente_1 = {}
for k, v in valori_scan.items():
    procente_1[k] = v[1] * 100 / maxim_1

procente_0 = {}
for k, v in valori_scan.items():
    procente_0[k] = v[0] * 100 / maxim_0

# transformam punctele procentuale in valori pe o scara de 30
valori_consola_1 = {}
for k, v in procente_1.items():
    valori_consola_1[f"{k}+{' ' * (max_k - len(k))}"] = int(30*(v/100))
# print(valori_consola_1)


valori_consola_0 = {}
for k, v in procente_0.items():
    valori_consola_0[f"{k}+{' ' * (max_k - len(k))}"] = int(30*(v/100))
print(valori_consola_0)


# printam
for k, v in valori_consola_1.items():
    l = "X" * v
    ll = "*" * valori_consola_0[k]
    print(f"{k}: {l}")
    print(f"{k}: {ll}")
