fruits = ('apple', 'banana', 'pear')

list_fruits = list(fruits)

list_fruits[1] = 'watermelon'

fruits = tuple(list_fruits)

print(fruits)

del fruits

print(fruits)