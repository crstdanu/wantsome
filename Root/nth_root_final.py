
number = input("please insert your number: ")[::-1]
n = int(input("Please insert the order of the root: "))


slices = []

for i in range(0, len(number), n):
    felie = number[i:i+n][::-1]
    slices.insert(0, felie)

#print(slices)

zeroes = [0, 0]

my_final_list = slices + zeroes
print(my_final_list)


