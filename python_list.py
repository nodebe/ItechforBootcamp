fruits = ["apple", "banana", "pear"]

random_list = ["kaykay", 23, ["apple", "pear"], fruits]

# print(fruits)

# print(random_list)

# print(fruits[3])

random_list[2][0] = "Pawpaw"

'''fruits.append("watermelon")
fruits.append("lemon")
print(fruits)'''
# random_list[0] = 'Metete'

# random_list.insert(1, 'Welete')
# print(fruits)
# fruits.pop(2)
# fruits.remove('lemon')

# del fruits

fruits.clear()

# print(fruits)

# print(random_list)

def sum_all(*numbers):
	total = 0
	for i in numbers:
		print(f'adding {i}')
		total+=i
	print(total)

sum_all(1,2,3,4,5,6,7,8)