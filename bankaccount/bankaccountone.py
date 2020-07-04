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


        
       
    
        
    


      
           
    




