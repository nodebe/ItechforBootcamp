fruits = ['apple', 'banana', 'watermelon','cherry','orange']

students = [{'name':'Ikem', 'department':'ECE', 'score':60, 'attendance':'Yes'},{'name':'Cheta', 'department':'ECE', 'score':75, 'attendance':'Yes'},{'name':'Emma', 'department':'ELE', 'score':40, 'attendance':'No'},{'name':'Presh', 'department':'ECE', 'score':25, 'attendance':'Yes'}]

passed_list = []
failed_list = []
not_valid_list = []

'''x = 0

while x < len(fruits):
	print(f'{x+1}. {fruits[x]}')
	x+=1'''

x = 0

while x < len(students):
	if students[x]['attendance'] == 'Yes':
		if students[x]['score'] >= 50:
			passed_list.append(students[x])
		else:
			failed_list.append(students[x])
		x+=1
	else:
		not_valid_list.append(students[x])
		x+=1
		continue


print("Passed")

j = 0

while j < len(passed_list):
	print(f"{passed_list[j]['name']} : {passed_list[j]['score'] + 5}")
	j+=1

print('\n')

print("Failed")

k = 0

while k < len(failed_list):
	print(f"{failed_list[k]['name']} : {failed_list[k]['score'] + 5}")
	k+=1

print('\n')

print("Not Valid")

y = 0

while y < len(not_valid_list):
	print(f"{not_valid_list[y]['name']} : {not_valid_list[y]['score']}")
	y+=1


print('\n')

a = 0

while a < 10:
	if a == 5:
		break
	print(f'This is {a}')
	a+=1
