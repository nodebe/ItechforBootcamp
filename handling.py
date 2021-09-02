'''try:
	num = int(input('How old are you: '))
	print(num + 5)
except ValueError as e:
	print("You can only pass in numbers. Try again!")
except:
	print("You have made a mistake!")
else:
	print('You are good to go!')
finally:
	print('You have entered the finals!')'''


def even_odd(a):
	try:
		if int(a) % 2 == 0:
			print(f'{a} is an even number!')
		else:
			print(f'{a} is an odd number!')
	except:
		print('You can only pass in numbers. Try again!')

num = input('What is your number: ')

even_odd(num)