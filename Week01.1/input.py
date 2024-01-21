# Taking input
num1 = input("Enter  first number: ")   
num2 = input("Enter second number: ")

# Addition
sum = float(num1) + float(num2)

# Subtraction
minus = float(num1) - float(num2)

# Multiplication
mul = float(num1) * float(num2)

# Division
div = float(num1) / float(num2)

# Modulus
mod = float(num1) % float(num2)

# Exponentiation
exp = float(num1) ** float(num2)

# Floor division
fdiv = float(num1) // float(num2)

# The "input" function takes data as a string. The input is treated as a string by default
# The "float" function transforms the string into a number with one decimal
# The "int" function transforms the string into an integer - a number without decimals
# So, we can allways replace "float" with "int" in our example

print("The sum of {0} and {1} is: {2}" .format(num1, num2, sum))
print("The subtraction of {0} and {1} is: {2}" .format(num1, num2, minus))
print("The multiplication os {0} and {1} is: {2}" . format(num1, num2, mul))
print("The division of {0} and {1} is: {2}" .format(num1, num2, div))
print("The modulus of {0} and {1} is: {2}" .format(num1, num2, mod))
print("The exponentiation of {0} and {1} is: {2}" .format(num1, num2, exp))
print("The floor division of {0} and {1} is: {2}" .format(num1, num2, fdiv))

