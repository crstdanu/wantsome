op = input("Operatia: ")

# while op not in ("+", "-", "/", "*"):
while not (op == "+" or op == "*" or op == "-" or op == "/"):
    op = input("introduceti operatia corecta: ")
    # statements under while

print(f"Ati introdus corect operatia: {op}")

# statements outside while
print("Game over")
