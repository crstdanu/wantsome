

# a = deimpartit
# b = divizor sau impartitor
# daimpartit / divizor = cat

a = int(input("\nIntroduceti numarul: "))
b = int(input("\nIntroduceti divizorul: "))

deimpartit = a
divizor = b
cat = 0
rest = 0

while True:
    if a >= b:
        a = a - b
        cat += 1
    else:
        rest = a
        break

print(f"\nNumarul {deimpartit} impartit la {divizor} rezulta catul {cat} si restul {rest}.\n")


