class BankAccount:
	'Base class for our Employees'
	
	def __init__(self, my_initial_balance):
		self.balance = my_initial_balance
		
	def get_balance(self):
		return self.balance
		
	
def main():
	#Create new bank account
	account = BankAccount(500)
	print('Current balance $', account.get_balance())
	
	account.balance += 800000	
	print('New balance $', account.get_balance())
	
	
main()
