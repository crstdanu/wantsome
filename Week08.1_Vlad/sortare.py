numere = [chr(n) for n in range(ord('0'), ord('0')+10)]
litere = [chr(n) for n in range(ord('a'), ord('a')+26)]
semne = [chr(n) for n in range(ord(" "), ord(" ")+16)] + [chr(n) for n in range(ord(":"), ord(":")+7)] + [chr(n)
                                                                                                          for n in range(ord("["), ord("[")+6)] + [chr(n) for n in range(ord("{"), ord("{")+4)]


colectie = {
    "numere": {},
    "litere": {},
    "semne": {},
    "alte_caractere": {}
}


with open("Week8.1_Vlad/wiatrace.log") as f:
    for linie in f.readlines():
        linie.strip()
        for caracter in linie:
            if caracter.lower() in litere:
                if caracter.lower() in colectie["litere"].keys():
                    colectie["litere"][f"{caracter.lower()}"] += 1
                else:
                    colectie["litere"][f"{caracter.lower()}"] = 1
            elif caracter in numere:
                if caracter in colectie["numere"].keys():
                    colectie["numere"][f"{caracter}"] += 1
                else:
                    colectie["numere"][f"{caracter}"] = 1
            elif caracter in semne:
                if caracter in colectie["semne"].keys():
                    colectie["semne"][f"{caracter}"] += 1
                else:
                    colectie["semne"][f"{caracter}"] = 1
            else:
                if caracter in colectie["alte_caractere"].keys():
                    colectie["alte_caractere"][f"{caracter}"] += 1
                else:
                    colectie["alte_caractere"][f"{caracter}"] = 1

# print(colectie.items())

for elem in colectie.keys():
    colectie[elem] = dict(sorted(colectie[elem].items()))

for key, value in colectie.items():
    print(f"{key}: {value}")
