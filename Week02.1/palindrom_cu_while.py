

numar = int(input("Please enter your number: "))  # asta se modifica cat timp ruleaza while

comparatie = numar  # asta nu se modifica cat timp ruleaza while

invers = 0

while (numar > 0):
    modulus = numar % 10
    invers = (invers * 10) + modulus
    numar = numar // 10



if (comparatie == invers):
    print("\nAm dat lovitura!")
else:
    print("\nE nasol tura asta!")


