

# suma primelor numere naturale

# initializare

n = int(input("Cate elemente?"))
s = 0
x = 1

# procesare
while x <= n:
    s = s + x
    x = x + 1

print(s)


# output (1+2+3+4+...+n)