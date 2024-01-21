fruits = ["apple", "banana", "cherry", "date", "elderberry"]
for fruit in fruits:
    if len(fruit) < 6:
        continue
    print(fruit)

# 0: fruit = apple
# 1: fruit = banana -> print(banana)
# 2: fruit = cherry -> print(cherry)
# 3: fruit = date
# 4: fruit = elderberry -> print(elderberry)
