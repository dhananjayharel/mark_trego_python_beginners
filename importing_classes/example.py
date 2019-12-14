import savings_account
import checking_account
		

	
def main():
	#Create new account
	mySavingsAccount = savings_account.SavingsAccount(300)
	myCheckingAccount = checking_account.CheckingAccount(500)
	
	#print initial balance
	print('Savings account balance: $', mySavingsAccount.get_balance())
	print('Checking account balance: $', myCheckingAccount.get_balance())
	
main()
