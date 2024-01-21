
print("For Celsius to Fahrenheit type: 1")
print("For Fahrenheit to Celsius type: 2")

print()
choice = int(input("Make your choice (1 or 2): "))
print()

if choice == 1:
    input1 = input("Insert Celsius degrees to convert: ")
    output1 = (float(input1) * 9 / 5) + 32
    print(f"{input1} degree Celsius equal to {output1} degree Fahrenheit")
if choice == 2:
    input2 = input("Insert Fahrenheit degrees to convert: ")
    output2 = (float(input2) - 32) * 5 / 9
    print(f"{input2} degree Fahrenheit equal to {output2: .2f} degree Celsius")
else: print("Invalid choice!")
print()



