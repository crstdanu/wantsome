
print()
# [::] - incepe la inceput si se termina la sfarsit
# [::-1] - incrementul e -1, adica schimba ordinea, de la sfarsit la inceput
num = input("Please insert your number: ")[::-1]
n = int(input("Please insert the root order: "))
# print(num)
# print(type(num))
# print(n)
# print(type(n))


# reversed_num = reversed(num)
# print(reversed_num)
print()
# cum tai felii de la x la y?
# variabila = s[2:5] - tai o felie de la pozitia 2 pana la pozitia 4

def cut_slices(num, n):
    slices = []
    # range (start, finish, increments)
    # or (start, stop, step)
    # incepe la 0, se termina la lungimea lui num (de ex: 10 caractere), in incremente de cate n
    for i in range(0, len(num), n):
        felie = num[i:i+n][::-1]  # prima tai fell iar a doua le inversez datele
        # aici introduc variabila la inceputul listei ca sa imi corespunda cu ordinea mea
        slices.insert(0, felie)
    # for every i in range return a value to the "slices" list    
    return slices
    



result = cut_slices(num, n)
result.extend("00")
print(result)

print(type(result))

print()



