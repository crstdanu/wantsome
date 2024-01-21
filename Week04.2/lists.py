my_list = [1, 2, 3, 1]
print(my_list.count(1))

# some_string = "whatever"
# print("Original string: ", some_string)
# print("Capitalized string: ", some_string.capitalize())
# print("e freq: ", some_string.count('e'))
print("adresa initiala:", id(my_list))
my_list = my_list + [1]
print(f"1. adr: {id(my_list)}", my_list)
my_list = [2] + my_list
print(f"2. adr: {id(my_list)}", my_list)
my_list.append(2)
print(f"3. adr: {id(my_list)}", my_list)

del(my_list[0])
print(f"4. adr: {id(my_list)}", my_list)
primul_elem = my_list.pop(0)
print(f"5. adr: {id(my_list)}", my_list, "primul elem:", primul_elem)
#  0  1  2  3  4    
# [2, 3, 1, 1, 2]
index_of_1 = my_list.index(1) # != [1]
print("index of 1:", index_of_1)
