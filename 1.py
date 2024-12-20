class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance
        
    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")
        
    def get_balance(self):
        return self.__balance
    
    def first_balance(self):
        self.__balance = 0
    
    def print_balance(self):
        print(self.__balance)
    
account = BankAccount()
account.first_balance()
account.print_balance()
account.deposit(50)
account.print_balance()