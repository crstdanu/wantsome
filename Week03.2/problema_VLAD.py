# cum sa aflam ultimele doua cifre ale unui numar la orice putere

Q = []
n = 5
exponent = 99

rezultat = n ** exponent
print(rezultat)
print('rezultat=', str(rezultat)[-1])

for e in range(20):
    r = n ** e
    rs = str(r)
    Q = Q + [int(rs[-1])]

print(Q)

unice = []
for el in Q:
    if el not in unice:
        unice += [el]

print(unice)

F = []
for el in unice:   # pentru fiecare element dintr-o lista sa faca o noua lista cu frecventa acelui element
    F += [Q.count(el)]

print(F)

maxim = max(F)
# print(maxim)

B = []
for index in range(len(unice)):
    if F[index] >= maxim-1:
        B = B + [unice[index]]

print('B=', B)
# print(A)

par_impar = n % 2
if par_impar == 0:
    if len(B) == 1:
        index_B = exponent % len(B)
    else:
        index_B = exponent % len(B) - 1
else:
    index_B = exponent % len(B)
# ---------------------------------------------

rezultat_final = B[index_B]
print(rezultat_final)
