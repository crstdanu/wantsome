#1. Demo
#   a) se genereaza random o parola string ascii folosind:
#     - alfabetul [a-z] cu 6/7 caractere
#	  - alfabetul [0-9] cu 8/9 cifre
#	  - alfabetul [a-zA-Z0-9] cu 5/6 caractere
#   b) incerc sa fac brute-force la parola random   
#
#2. Problema
#   Dandu-se o arhiva protejata cu o parola care foloseste cel mai extins dintre cele 3 alfabete, construim un script care sparge parola
import random
import time
def genereaza_09_2(n):
    m = [random.choice(range(10)) for _ in range(n)]    
    print(m)

def genereaza_09_1(n):
    start = 10 ** (n-1)
    stop = 10 ** n
    nr = random.choice(range(start, stop))
    return nr

def genereaza_az(n):
    m = [chr(ord('a') + random.choice(range(26))) for _ in range(n)]   
    passw = "".join(m) 
    return passw

def GenereazaParola_az(K, n):
    l = []
    for i in range(n):
        index = (K // (26**(n-1-i))) % 26
        l += [chr(ord('a') + index)]
    return "".join(l)
        

#l = [genereaza_09_1(5) for _ in range(10)]
#print(l)
#genereaza_09_2(3)
#genereaza_az(4)
#genereaza_az(7)
passw = genereaza_az(5)
start = time.time()
for i in range(26**5):
    passw_crt = GenereazaParola_az(i, 5)
    if passw_crt == passw:
        print(f"Ai ghicit in {i} incercari: {passw}")
        break
stop = time.time()
print(stop-start)