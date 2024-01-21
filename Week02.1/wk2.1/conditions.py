year = input("Year to check: ")
year = int(year)

# one line aternative solution:
# year = int(input("Year to check: "))

if year % 4 == 0 and year % 100 != 0:
    print(f"{year} este an bisect 1")
elif year % 400 == 0:
    print(f"{year} este an bisect 2")
else:
    print(f"{year} nu este an bisect")

print("Game over")
