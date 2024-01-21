number1 = 5
number2 = 3

sum=number1+number2     # Adds two values
product=number1*number2     # The product of number1 and number2
div=number1/number2     # The quotient when the first number is divided by second
diff=number1-number2     # Substraction of number2 from number1
exp=number1**number2  # Exponentiation multiplies number1 by itself number2 times
fdiv=number1//number2   # Floor division shows division with fraction removed
mod=number1%number2    # Modulus - shows only the remainder of the division

print("The sum of", number1, "and", number2, "is:", sum)
print("The product of", number1, "and", number2, "is:", product)
print("the quotient of", number1, "and", number2, "is:", div)
rounded_div=round(div, 2)
print("The rounded quotient of", number1, "and", number2, "is:", rounded_div)
print("the difference between", number1, "and", number2, "is:", diff)
print("The exponentiation of", number1, "and", number2, "is:", exp)
print("The floor division between", number1, "and", number2, "is:", fdiv)
print("The remainder of", number1, "and", number2, "is:", mod)
