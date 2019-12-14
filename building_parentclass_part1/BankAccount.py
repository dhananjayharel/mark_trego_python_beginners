class BankAccount: # Parent class
	
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
	#Create new account
	account = BankAccount(200)
	
	# Display the current balance of the account
	print('Account balance: $', account.get_balance())	

	
	
main()
