# Ex 2
# Testeaza perfomanta conexiunii tale la internet
# Folosind requests, descarca urmatorul fisier de 100 de ori, cronometreaza timpul de descarcare si la final afiseaza
# timpul minim de descarcare, cel maxim si media
# https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js


import requests
from datetime import datetime as dt

url = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"

lista_timestamp = []
descarcari = 100
for i in range(descarcari):
    raspuns = requests.get(url)
    now = dt.now()
    lista_timestamp.append(now)


lista_diferente = []
for i in range(len(lista_timestamp[:-1])):
    diferenta = lista_timestamp[i+1] - lista_timestamp[i]
    lista_diferente.append(diferenta.microseconds)

timp_total = 0
for elem in lista_diferente:
    timp_total += elem

print(
    f'\nTimp total: {timp_total/1000000:.2f} secunde pentru {descarcari} descarcari')
print(f'Media: {(timp_total/(1000*descarcari)):.2f} milisecunde/descarcare')

timp_minim = min(lista_diferente)
timp_maxim = max(lista_diferente)

print(f'Timpul minim: {(timp_minim/1000):.1f} ms')
print(f'Timpul maxim: {(timp_maxim/1000):.1f} ms')
