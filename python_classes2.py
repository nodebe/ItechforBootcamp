class ItechBank():

	def __init__(self, name, balance):
		self.name = name
		self.balance = balance

	def check_balance(self):
		# self.balance-=10
		print(f'Your balance is N{self.balance}')

	def deposit(self, amount, depositor):
		self.balance+=amount
		print(f'{depositor} paid in N{amount} to your account. Your new balance is N{self.balance}')

	def withdraw(self, amount):
		if amount < 1000:
			print('Minimum amount for withdrawal is N1000')
			return False
		else:
			if self.balance >= amount:
				self.balance-=amount
				print(f'N{amount} was withdrawn from your account. Your new balance is N{self.balance}')
				return True
			else:
				print('Insufficient balance!')
				return False

	def transfer(self, amount, user):
		if self.withdraw(amount):
			user.deposit(amount, self.name)

user1 = ItechBank('Ikem Nodebe', 2000)
user2 = ItechBank('Charles', 3000)

# user1.check_balance()
# user2.check_balance()

# user1.deposit(3000, 'Emma')

# user1.withdraw(500)

user1.transfer(1500, user2)