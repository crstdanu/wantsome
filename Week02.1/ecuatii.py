print()
number1 = input("Chose first number: ")
number2 = input("Chose second number: ")

num1 = int(number1)
num2 = int(number2)

print("Choose your operation:\nFor adition type 1\nFor subtraction type 2\nFor multiplication type 3\nFor division type 4\n\n")

choise = int(input(" Insert your choice: "))

if choise == 1:
    print(num1 + num2)
elif choise == 2:
    print(num1 - num2)
elif choise == 3:
    print(num1 * num2)
else:
    print(num1 / num2)

print()

