fruits = ("apple", "banana", "pear")

one_fruit = ("lemon",)

# print(one_fruit)

# fruits[0] = "Lemon"

list_fruits = list(fruits)

print(list_fruits)

list_fruits[0] = 'lemon'

fruits = tuple(list_fruits)

print(fruits)

del fruits

print(fruits)