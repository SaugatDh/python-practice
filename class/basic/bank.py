class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder= account_holder
        self.balance=balance
    def deposit(self,amount):
        if amount<0:
            print("Deposit amount must be positive")
            return
        self.balance = self.balance+amount
        print("Deposited amount is Rs.",amount)
        print("Total balance is Rs.",self.balance)
    
    def withdraw(self,amount):
        if amount<0: return
        if amount> self.balance:
            print("Insufficient fund.")
        self.balance=self.balance-amount
        print("Withdrawn amount is Rs.",amount)
        print("New balance is Rs.",self.balance)
    
    def displayBalance(self):
        print("Account Holder: ",self.account_holder)
        print("Balance: ",self.balance)
        
account=BankAccount("Saugat",10000)
account.displayBalance()

account.deposit(500)
account.withdraw(200)
    
        
        