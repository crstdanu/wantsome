# Formula lui Fibonacci
# Daca sunt date 2 numere x1 si x2 3
# F0 = 0
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21

pahar_unu = 0
pahar_doi = 1
pahar_gol = 1
 
numar = int(input("Introduceti ordinul lui Fibonacci: "))

ordin = 2

while ordin <= numar:
    pahar_doi = pahar_doi + pahar_unu
    pahar_unu = pahar_gol
    pahar_gol = pahar_doi
    ordin += 1


print(f"Acesta este numarul Fibonacci: {pahar_doi}")


