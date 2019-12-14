class BankAccount:

    # The init method initializes the 
	# data members with the arguments
	
	def __init__(self, firstName, lastName, account_number, xBalance):
		self.__first_name = firstName
		self.__last_name = lastName
		self.__account_num = account_number
		self.__balance = xBalance
		
	def get_account_details(self):
		print('First name:', self.__first_name)
		print('Last name:', self.__last_name)
		print('Account umber:', self.__account_number)
		print('Balance:', self.__balance)		
		print()
		
		def get_balance(self):
		return self.__balance
		
	def deposit(self, amount_to_deposit):
		self.__balance += amount_to_deposit	
		
		
	
def main():

	#Create new account details
	account_01 = BankAccount('Victor', 'Devis', '5632', 300)
	account_02 = BankAccount('Jason', 'Wilson', '7852', 600)
	account_03 = BankAccount('Scott', 'James', '4112', 200)
	

	#Display account details for each account		
	account_01.get_account_details()
	account_02.get_account_details()
	account_03.get_account_details()
	
	
	
main()
