class BankAccount:
	'Base class for our Employees'
	
	def __init__(self, my_starting_balance):
		self.__balance = my_starting_balance
		
	def get_balance(self):
		return self.__balance
		
	def deposit(self, amount_to_deposit):
		self.__balance += amount_to_deposit	

	def withdraw(self, amount):
		self.__balance -= amount

class SavingsAccount(BankAccount): # Child class from BankAccount
	def __init__(self, initial_balance):
		BankAccount.__init__(self,initial_balance)
		

	
def main():
	#Create new savings account
	savings_account = SavingsAccount(200)
	
	# Display the current balance of the account
	print('Savings account balance: $', savings_account.get_balance())	
	savings_account.deposit(300)
	print('New balance $', savings_account.get_balance())
	savings_account.withdraw(450)
	print('Savings account balance after withdraw: $', savings_account.get_balance())	
	
	
main()
