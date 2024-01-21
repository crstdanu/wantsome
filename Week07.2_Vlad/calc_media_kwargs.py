note = {
    "George": {
        "Romana": 9.5,
        "Matematica": 7.5,
        "Germana": 6
    },
    "Mihai": {
        "Romana": 7,
        "Matematica": 9,
        "Franceza": 8.4
    },
    "George": {
        "Romana": 9.2,
        "Matematica": 9,
        "Germana": 5
    },
    "Vlad": {
        "Romana": 8.2,
        "Matematica": 9,
        "Franceza": 6.5
    }

}


def calculeaza_media(elev, **kwargs):
    count = 0
    suma_note = 0
    for note in kwargs.values():
        suma_note += note
        count += 1
    media = suma_note / count
    print(f"Elevul {elev} are media {media:.2f}")


for elev, catalog in note.items():
    calculeaza_media(elev, **catalog)
