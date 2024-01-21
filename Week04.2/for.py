my_list = [2, 34, 1, 0, -1, 6, 10]
max_nr = max(my_list)
min_nr = min(my_list)
print(max_nr, min_nr)

minim = my_list[0]
maxim = my_list[0]
# minim = maxim = my_list[0]
print(maxim, minim)
for element in my_list[1:]:         # matematica: [1, 3) = 1, 2
    if element > maxim:
        maxim = element
    if element < minim:
        minim = element

print(maxim, minim)

# minim = 2, maxim = 2
# ----------------------
# Iteratii:
# 0: element = 2, minim = 2, maxim = 2
# 1: element = 34, minim = 2, maxim = 34
# 2: element = 1, minim = 1, maxim = 34
# 3: element = 0, minim = 0, maxim = 34
# 4: element = -1, minim = -1, maxim = 34
# 5: element = 6, minim = -1, maxim = 34
# 6: element = 10, minim = -1, maxim = 34

