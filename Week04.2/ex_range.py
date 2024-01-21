# range syntax: range(start, end, step)
# for num in range(2, 21):
#     for div in range(2, num):
#         if num % div == 0:
#             break
#     else:
#         print(num)      # numarul este prim


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for line in matrix:
    for line_elem in line:
        print(line_elem, end="\r")
