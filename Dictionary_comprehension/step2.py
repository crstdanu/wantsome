auto = [
    {
        "nume": "A3",
        "producator": "Audi",
        "an_fabricatie": "2010",
        "optiuni_motor": [1.4, 1.6, 1.8, 2.0],
        "optiuni_combustibil": ["motorina", "benzina"]
    }]


output = [{key: (auto[0]["nume"] if key == "nume" else auto[0]["producator"] if key == "producator" else auto[0]["an_fabricatie"] if key == "an_fabricatie" else auto[0]["optiuni_combustibil"] if key == "optiuni_combustibil" else auto[0]["optiuni_motor"][i]) for key in auto[0]}
          for i in range(len(auto[0]["optiuni_motor"]))]

print(output)

final = [{} for x in range(len(auto[0]["optiuni_combustibil"]))]
print(final)
