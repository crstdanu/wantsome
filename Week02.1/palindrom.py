

number_input = input("Insert your number: ")

palindrom = int(number_input[::-1])
number = int(number_input)


condition = bool(True)

if number == palindrom:
    condition = True
else:
    condition = False

print(f"Numarul introdus este polindrom: {condition}")