

print()
print("Daca introduci un numar iti arat numarul de divizori ai acelui numar")
print()
numar = int(input("Introduceti numarul: "))

count = 1
x = 1

while x < numar:
    if numar % x == 0:
        count +=1
    x += 1

print(f"\nNumarul de divizori ai lui {numar} este: {count}")