
suma = 0
medie = 0
contor = 0

while True:
    numar = int(input("\nIntroduceti un numar ca sa continui\nsau ZERO ca sa terminam: "))
    if numar > 0:
        contor += 1
        suma += numar
        medie = suma / contor
        print(f"\nAi introdus {contor} numere. Media este: {round(medie, 2)}")
    else:
        break