import math


'''def calc():
	x = 5+4
	return x

y = calc()

bitcoin_amount = 30000
def call_me():
	#call me when bitcoin rises
	pass

if bitcoin_amount > 40000:
	call_me()

'''

'''def calc(b, c):
	a = b+c
	return a

print(calc(3, 4))'''

'''def intro(name='Cheta', age=26, department='MME'):
	print(f'Your name is {name}, you are {age} years old and you are in {department}')

intro(department="ECE")'''


def almighty(a, b, c):
	top = abs(b**2 - (4*a*c))
	d = (-b + math.sqrt(top))/2*a
	e = (-b - math.sqrt(top))/2*a
	x = (d,e)
	return x

print(almighty(1,2,3))