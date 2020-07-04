import time

# creating a bank account where a user can deposit and withdraw funds 
# creating and initialisng the class 

class BankAccount:
    def __init__(self):
        self.balance = 0
# the function takes the amount you put in as a deposit
    def deposit(self,amount):
        self.balance = self.balance + amount

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount  # self.balance = self.balance - amount
        else:
            print("Insufficient funds")
    
    def print_balance(self):
        return self.balance

class SavingAccount(BankAccount):
    def __init__(self):
        self.balance = 0
    
    def deposit(self,amount):
        self.balance = self.balance + amount
    
    def accrue_interest(self, rate_of_interest=0.02):
        while True:
            self.balance = self.balance*(1+rate_of_interest)
            time.sleep(10)

    def print_balance(self):
        return self.balance

        
       
account = BankAccount()
account.deposit(35000)
account.withdraw(1000)
print(account.print_balance())

savings_account = SavingAccount()
savings_account.deposit(2000)
savings_account.accrue_interest(0.02)
print(savings_account.print_balance())
        
    


      
           
    




