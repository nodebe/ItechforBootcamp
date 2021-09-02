fruits = ['apple', 'banana', 'pear']

random_list = ['Kaykay', 24, ['watermelon', 'pawpaw'], fruits]

# print(random_list)

# print(fruits)

# new_fruit = input("Put your new fruit: ")

# fruits[0] = new_fruit

# random_list[2][0] = input("Put your newest fruit: ")

# print(random_list)

# new_fruit = input("Your new fruit: ")

# fruits.append(new_fruit)
# fruits.append('cherry')


fruits.insert(0, 'orange')

# print(fruits)

to_do_list = ['wash plates', 'learn python', 'read book']

# print(to_do_list)


# task = input("What is the task: ")
# position = int(input("What position do you want it added: "))

# to_do_list.insert(position-1, task)

# print(to_do_list)

# to_do_list.pop(1)

# to_do_list.remove("learn python")

# to_do_list.clear()

# del to_do_list

# print(to_do_list)

def sum_all(*numbers):
	total = 0

	for i in numbers:
		total+=i
		
	print(total)


sum_all(1,2,3,4,5,6,7)