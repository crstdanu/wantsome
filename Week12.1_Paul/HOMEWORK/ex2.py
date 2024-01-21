# Ex 2
# Testeaza perfomanta conexiunii tale la internet
# Folosind requests, descarca urmatorul fisier de 100 de ori, cronometreaza timpul de descarcare si la final afiseaza
# timpul minim de descarcare, cel maxim si media
# https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js


import requests
import datetime

url = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"

lista_timpi = []

for cont in range(10):
    cont = requests.get(url)
    with open("index.html", "wb") as f:
        f.write(cont.content)
    now = datetime.datetime.now()
    lista_timpi.append(now.strftime("%H-%M-%S"))

lista_diferente = []
for i in range(len(lista_timpi[:-1])):
    time_inceput = datetime.datetime.strptime(lista_timpi[i], "%H-%M-%S")
    time_sfarsit = datetime.datetime.strptime(lista_timpi[i+1], "%H-%M-%S")
    diferenta = time_sfarsit - time_inceput
    lista_diferente.append(diferenta.seconds)

timp_total = 0
for elem in lista_diferente:
    timp_total += elem

print(timp_total)

timp_minim = min(lista_diferente)
timp_maxim = min(lista_diferente)

print(timp_minim)
print(timp_maxim)
