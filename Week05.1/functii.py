
def f(x):
    return 3 * x + 2


def g(x):
    return x + 1


def h(x):
    return 2 * x - 3


def w(x):
    return f(h(g(x)))


xxl = w(10)
print(xxl)
