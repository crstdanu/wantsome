# Ex 2
# Testeaza perfomanta conexiunii tale la internet
# Folosind requests, descarca urmatorul fisier de 100 de ori, cronometreaza timpul de descarcare si la final afiseaza
# timpul minim de descarcare, cel maxim si media
# https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js


import requests
import time

url = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"

lista_timestamp = []
descarcari = 100
for i in range(descarcari):
    raspuns = requests.get(url)
    now = time.time()
    lista_timestamp.append(now)


lista_diferente = []
for i in range(len(lista_timestamp[:-1])):
    diferenta = lista_timestamp[i+1] - lista_timestamp[i]
    lista_diferente.append(diferenta)


timp_total = lista_timestamp[-1] - lista_timestamp[0]

print(
    f'\nTimp total: {timp_total:.2f} secunde pentru {descarcari} descarcari')
print(f'Media: {(timp_total/descarcari):.3f} secunde/descarcare')

timp_minim = min(lista_diferente)
timp_maxim = max(lista_diferente)

print(f'Timpul minim: {(timp_minim):.3f} s')
print(f'Timpul maxim: {(timp_maxim):.3f} s')
