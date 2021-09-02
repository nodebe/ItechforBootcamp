import random

def guessing_game():
	number = random.randrange(0, 101)
	user_guess = int(input("What is your number: "))

	if user_guess > number:
		print("Too high!")
	elif user_guess < number:
		print("Too low!")
	else:
		print('Just right!')

	print("Generated number is {0}".format(number))

guessing_game()
