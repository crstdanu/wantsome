#         -7  -6 -5 -4  -3 -2 -1 
# indexes  0   1  2  3   4  5  6 
my_list = [2, 34, 1, 0, -1, 6, 10]

# slicing sintax: mylist[start:stop:step]

print("1 to end", my_list[1:])
print("start to 4", my_list[:5])
print("1 to 5", my_list[1:6])
print("1 to 5, step 2", my_list[1:6:2])
print("full list, backwards", my_list[::-1])
print("2 to 4, backwards", my_list[5:1:-1])
