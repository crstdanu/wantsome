import json

data = json.load(open('input.json', 'r'))
print(data)

numere = data['numere']
maxim = max(numere.values())
print(maxim)

procente = {}

for i, (k, v) in enumerate(numere.items()):
    procente[k] = v / (maxim / 100)
print(procente)

valori_consola = {}
for i, (k, v) in enumerate(procente.items()):
    valori_consola[k] = int(30 * (v/100))
print(valori_consola)

for i, (k, v) in enumerate(valori_consola.items()):
    l = ['*'] * v
    print(f'{k} : {"".join(l)}')

aranjate = {}
for i, (k, v) in enumerate(valori_consola.items()):
    aranjate[k] = [' '] * (30-v) + ['*'] * v
# for i,(k,v) in enumerate(aranjate.items()):
#    print(k,"".join(v))
sortate = dict(sorted(aranjate.items()))
for i in range(30):
    linie = ""
    for j, (k, v) in enumerate(sortate.items()):
        linie += v[i]
    print(linie)
