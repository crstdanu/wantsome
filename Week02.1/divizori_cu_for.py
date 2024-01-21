
print()
print("Daca introduci un numar iti arat numarul de divizori ai acelui numar")
numar = int(input("Introduceti numarul: "))

count = 1
x = 1

for n in range(1, numar):
    if numar%n == 0:
        count +=1

print(f"Numarul de divizori ai lui {numar} este: {count}")
