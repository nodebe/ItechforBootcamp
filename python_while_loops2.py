'''x = 1

while x < 10:
	print(x)
	x+=1
'''

fruits = ['apple', 'banana', 'cherry', 'mango', 'orange', 'berry']

x = 0

'''while x < len(fruits):
	if fruits[x] == 'mango':
		x+=1
		continue
	print(f"{x+1}. {fruits[x]}")
	x+=1'''

students = [{'name':'Kaykay','attendance':'yes'},{'name':'presh','attendance':'yes'},{'name':'cheta','attendance':'no'},{'name':'mark','attendance':'yes'},{'name':'chisom','attendance':'no'}]

valid = []
not_valid = []

j = 0

'''while j < len(students):
	if students[j]['attendance'] == 'no':
		j+=1
		continue
	valid.append(students[j])
	j+=1

k = 0

while k < len(valid):
	print(valid[k])
	k+=1'''

j = 0

'''while j < 10:
	print(j)
	if j == 7:
		break
	j+=1'''

while j < 10:
	if j % 2 == 0:
		j+=1
		continue
	print(j)
	j+=1