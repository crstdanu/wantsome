print()
print("To convert from Celsius to Fahrenheit")
input1 = input("Please, enter the temperature in Celsius: ")
# acum input1 e string
type(input1)
# il fac numar, ca sa il pot calcula, cu functia float sau cu int 

output1 = (float(input1) * 9/5) + 32

print_output1 = f"{input1} degree Celsius equal to {output1: .1f} degree Fahrenheit"
print(print_output1)
print()

print("Let's try the other way")
input2 = input ("Enter the temperature in Fahrenheit: ")
output2 = (float(input2) - 32) * 5/9
print_output2 = f"{input2: .1f} degree Fahrenheit equal to {output2: .1f} degree Celsius"
print(print_output2)
print()
