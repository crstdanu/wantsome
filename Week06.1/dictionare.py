import json

dct = {
    "chieia1": "valoarea1",
    "chieia1": "valoarea2",
    "k3": 100,
    "k4": 71.5,
    "k5": [10, 11, 12, 13],
    "k6": {
        "c1": 101,
        "c2": "Hello",
    },
    "k7": "Hello"
}

for i, (k, v) in enumerate(dct.items()):
    print(i, k, "--> ", v)


# f = open("fisier.json", "w")
# cu dump scriu
# json.dump(dct, f)

# with open("fisier.json", "w") as f:
#     json.dump(dct, f)

# json.dump(dct, open("new.json", "w"))

dct = json.load(open("fisier.json", "r"))

print(dct)
