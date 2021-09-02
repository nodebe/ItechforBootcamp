student = {'name':'Kaykay','age':25,'department':'ECE'}

# print(student['name'])

student['blood group'] = 'O+'

# print(student)

student.pop('name') # To remove a particular key - value

student.clear() # To delete every key - value pair in a dictionary

del student # To delete the dictionary entirely

# print(student)


def students(*args, **kwargs):
	print(args, kwargs)

name = input("what is your name: ")
age = int(input("How old are you: "))
department = input("What department are you: ")

students(1,2,3,4,5,name=name, age=age, department=department)