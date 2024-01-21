# Factorial
# f3 = 3 * f2(2 * f1)
# f4 = 4 * f3[3 * f2(2 * f1)]

numar = int(input("\nInsert your factorial number: "))

n = 1
factorial = 1

while n <= numar:
    factorial = n * factorial
    n += 1

print(f"\n{numar}'s factorial is: {factorial}\n")
