'''try:
	num = int(input('What is your number: '))
	print(num + 25)
except:
	print('There is a small problem!')
else:
	print('You are good to go!')
finally:
	print('We are at finally!')'''

def odd_even(num):
	if num % 2 == 0:
		print('even')
	else:
		print('odd')

try:
	number = int(input('Your number: '))
	odd_even(number)
except:
	print('Please insert only numbers!')