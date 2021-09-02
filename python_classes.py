class ItechBank():

	def __init__(self, name, balance):
		self.name = name
		self.balance = balance

	def check_balance(self):
		self.balance-=10
		print(f'Your balance is N{self.balance}')

	def deposit(self, amount, depositor):
		self.balance+=amount
		print(f'{depositor} paid in {amount} to your account. Your new balance is {self.balance}')

	def withdraw(self, amount):
		if self.balance >= amount:
			self.balance-=amount
			print(f'Your account has been deducted by {amount}. Your new balance is {self.balance}')
			return True
		else:
			print('Insufficient funds')
			return False

	def transfer(self, amount, user):
		if self.withdraw(amount):
			user.deposit(amount, self.name)

user1 = ItechBank('Ikem Nodebe', 2000)
user2 = ItechBank('Presh', 3000)

# user2.check_balance()

# user1.deposit(5000, 'Emma')

# user1.withdraw(4000)

user1.transfer(5000, user2)