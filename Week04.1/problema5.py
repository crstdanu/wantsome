
range_min = 0
range_max = 100


for x in range(range_min, range_max):
    for y in range(range_min, range_max):
        if (lambda x, y: 2*x-y == 4 and x + 3*y == -5):
            print(x, y)
