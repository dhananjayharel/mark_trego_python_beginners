import account_type

# Main method
def main():

    # Setup a checking acount and savings account.
    
    my_savings_account = account_type.SavingsAccount(0)
    my_checking_account = account_type.CheckingAccount(700)
  

    # Display the current balance for both accounts.
    
    print('Savings account balance: $', my_savings_account.get_balance())
    print('Checking account balance: $', my_checking_account.get_balance(), "\n")


    # Transfer money from checking account to savings account.

    my_savings_account.transfer(my_checking_account, 500)

    # Display new savings account balance and checking account
    # balance.
    print('Savings account balance: $', my_savings_account.get_balance())
    print('Checking account balance: $', my_checking_account.get_balance())
   
# Run program.
main()
