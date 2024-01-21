
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
# 1, 2, 3, 4, 5, 6,  7 , 8,  9, 10,

# primul = 0
# al_doilea = 1


def fibonacci(x):
    if x == 1:
        return 1
    if x == 2:
        return 1
    return fibonacci(x-1) + fibonacci(x-2)


n = 12
print(fibonacci(n))
