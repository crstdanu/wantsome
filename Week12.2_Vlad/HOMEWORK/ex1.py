# 1
# Folosind subprocess, executati comanda "ipconfig /all" si extrageti din output un dictionar de forma
# {
#     "ipconfig": [{
#         "name": "Wireless LAN adapter WiFi",
#         "description": "Intel(R) Dual Band Wireless-AC 8265",
#         "physical_address": "34-41-5D-3A-AB-7E",
#         "ipv4_address": "192.168.111.206"
#     }]
# }
# Veti avea cate un dictionar ca in exemplu pentru fiecare interfata pe care o returneaza comanda


import subprocess


out = subprocess.run('ipconfig /all', capture_output=True, text=True)


lista = out.stdout.split('\n\n')

lista_nume = [el.replace(':', '') for el in lista if "  " not in el]
lista_atribute = [el.split("\n") for el in lista if "  " in el]
print(lista_nume[4])
ce_am_nevoie = []

for elem in lista_atribute[4]:
    if 'Description' in elem:
        ce_am_nevoie.append(elem)
    if 'Physical' in elem:
        ce_am_nevoie.append(elem)
    if 'IPv4' in elem:
        ce_am_nevoie.append(elem)

ce_am_nevoie = [el.split(':').pop(1).strip() for el in ce_am_nevoie]


mydict = {'ipconfig': [{'name': lista_nume[4],
                        'description': ce_am_nevoie[0],
                        'physical_address': ce_am_nevoie[1],
                        'ipv4_address': ce_am_nevoie[2].replace("(Preferred)", "")}]}
print(mydict['ipconfig'])
