class BankAccount:
	'Base class for our Employees'
	
	def __init__(self, my_starting_balance):
		self.__balance = my_starting_balance
		
	def get_balance(self):
		return self.__balance
		
	def deposit(self, amount_to_deposit):
		self.__balance += amount_to_deposit	
	
def main():
	#Create new bank account
	account = BankAccount(600)
	print('Current balance $', account.get_balance())
	
	#try to hack balance
	#account.balance += 800000	
	
	account.deposit(50000)
	print('New balance $', account.get_balance())
	
	
main()
