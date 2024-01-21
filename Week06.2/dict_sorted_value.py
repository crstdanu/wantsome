my_dict = {'apple': 3, 'banana': 4, 'orange': 2}

# Sort the dictionary by values in decending order
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

print(sorted_dict)
