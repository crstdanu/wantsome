

user_nr = input(
    "\nInser your number and we'll place it on a list. Digit by digit! \nPlease insert your number: \n"
)

blacklist = list(user_nr)

blacklist = [int(n) for n in blacklist]  # list comprehension

print(blacklist)
