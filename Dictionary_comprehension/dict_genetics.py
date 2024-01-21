# A DICTIONARY OF LISTS

# A can only be paired with T while
# C can only be paired with G

# create strand 1 (list) with random bases
# create a pairable strand 2 (list) based on the values from strand 1
# create a dictionary with sequential keys
# assign each key to a pair of bases such that:
# { 0: [s1[0], s2[0]], ...}

import random

bases = ["A", "C", "G", "T"]

strand1 = random.choices(bases, k=10)
print(strand1)


# dna = {}
# for idx, b in enumerate(dna_st1):
#     if b == "A":
#         b2 == "T"
#     elif b == "T":
#         b2 == "A"
#     elif b == "C":
#         bs == "G"
#     else:
#         b2 == "C"
#     dna[idx = [b, b2]]

# each of the key represents an INDEX for a numeric sequence
# each of the values represent a pair of the bases (dna bases)
# the first item is taken from the strand1 list and the second one is assigned based on the conditions

dna = {key: [value, None] for (key, value) in enumerate(strand1)}
print(dna)

# we can't include an elif inside a dictionary comprehension so we use else toghether with if

dna = {key: [value,
             ("T" if value == "A" else "A" if value ==
              "T" else "G" if value == "C" else "C")
             ] for (key, value) in enumerate(strand1)}

print(dna)
