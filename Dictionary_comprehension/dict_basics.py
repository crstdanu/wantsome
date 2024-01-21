names = ["Cristian", "Gandalf", "Batman"]
profs = ["programmer", "wizard", "superhero"]


my_dict = {}

for (key, val) in zip(names, profs):
    my_dict[key] = val

# print(my_dict)


new_dict = {}

for i in range(len(names)):
    new_dict[names[i]] = profs[i]

print(new_dict)


another_dict = {
    key: value for (key, value) in zip(names, profs)
}
print(another_dict)

one_dict = {
    names[i]: profs[i] for i in range(len(names))
}

print(one_dict)
