
print()
print("Afla care este cel mai mare X, putere a lui 2, mai mic decat numarul tau")
print()
number = int(input("Introduceti numarul: "))
print()

n = 0
while 2**n <= number:
    n += 1

num = 2**(n-1)

print(
    f"Cel mai mare numar, putere a lui 2,\nmai mic sau egal decat numarul ales, \neste: {num}")
print()
