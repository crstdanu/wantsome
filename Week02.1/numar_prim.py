
print()
print("Vrei sa stii daca un numar este prim?")
print()
numar = int(input("Introduceti numarul: "))

count = 1
x = 1

for n in range(1, numar):
    if numar%n == 0:
        count +=1

# print(f"Numarul de divizori ai lui {numar} este: {count}")

if count <= 2:
    print(f"\nNumarul {numar} este PRIM.\n")
else:
    print(f"\nNUmarul {numar} NU este prim.\n")