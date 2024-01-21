

# Exemplu: a=7, b=11, n=5
#    7/11 = 0 r 7
#    (7*10)/11 = 6 r 4
#    (4*10)/11 = 3 r 7
#    (7*10)/11 = 6 r 4
#    (4*10)/11 = 3 r 7
#    (7*10)/11 = 6 r 4
#    Rezultat = 0,36363
user_deimpartit = input("\nIntroduceti deimpartitul: ")
user_impartitor = input("\nIntroduceti impartitorul: ")

a = int(user_deimpartit)
b = int(user_impartitor)
n = 5
new_list = []


while len(new_list) <= n:
    if len(new_list) == 0:
        new_list += [a // b]
        a = a % b
    else:
        new_list += [((a*10)//b)]
        a = (a*10) % b


# print(
#     f"\n{new_list[0]},{new_list[1]}{new_list[2]}{new_list[3]}{new_list[4]}{new_list[5]}"
# )

print(new_list)

new_list_str = [str(n) for n in new_list]
print(new_list_str)

zecimal = "".join(new_list_str[1:])
print(zecimal)
print(f"\n{new_list_str[0]},{zecimal}")

# element = str({new_list_str[0]}, {zecimal})


# print(element)
