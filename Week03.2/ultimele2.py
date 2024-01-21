

ultimele_doua = []
frecvente = []
x = 199
y = 37

unice = []
frecvente = []
counter = 0
operatii = 0

while counter < 10:
    x = x * y
    operatii += 1
    ultimele_doua += [x % 100]
    for nr in ultimele_doua:  # aici cream lista de elemnte unice
        if nr not in unice:
            unice += [nr]

    for element in unice:  # aici le numaram
        frecvente += [ultimele_doua.count(element)]
    # aici aflam cand un numar a ajuns la 10 frecvente
    counter = max(frecvente)


print(f"\nNumarul {ultimele_doua[-1]} apare de 10 ori")

print(f"\nExista {len(unice)} elemente unice in multime")
print(f"\nS-au facut {operatii} inmultiri\n")
print(unice)
