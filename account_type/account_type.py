class BankAccount: # Parent class
    'Base class for bank accounts.'

    # The __init__ method initializes the
    # balance attribute with a starting
    # balance.
    
    def __init__(self, starting_balance):
        self.__balance = starting_balance

    # Deposits money into an account.
    
    def deposit(self, amount):
        self.__balance += amount

    # Withdraws money from an account.
    
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Inefficient Funds!!!\n")
        else:
            self.__balance -= amount

    # Retrieves the current balance of
    # the given account.
    
    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount): # child class of BankAccount

    def __init__(self, savings_account_balance):
        # Call the BankAccount class __init
        # method and initialize the data
        # attribute "balance".
        BankAccount.__init__(self, savings_account_balance)

    def transfer(self, account_obj, amount):
        if amount <= account_obj.get_balance():
            account_obj.withdraw(amount)
            self.deposit(amount)
            print('Transferred $', amount, "into your savings account.\n")
        else:
            print("Inefficient Funds!!!\n")

class CheckingAccount(BankAccount): # child class of BankAccount

    def __init__(self, initial_balance):
        # Call the BankAccount class __init
        # method and initialize the data
        # attribute "balance".
        BankAccount.__init__(self, initial_balance) 
