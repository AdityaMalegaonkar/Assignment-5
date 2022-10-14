# Assignment - 5

# 5. Handling a Bank Account

class account:
    def __init__(self , title = None , balance = 0):
        self.title = title
        self.balance = balance

    def withdrawal(self , amount):
        self.amount = amount
        self.balance -= amount

    def deposit(self , amount):
        self.amount = amount
        self.balance += amount

    def get_balance(self):
        print("Account Balance :" , self.balance)

    def display(self):
        print("(" , self.title , "," , self.balance , ")")

class savingsaccount(account):
    def __init__(self , title = None , balance = 0 , interestrate = 0):
        super().__init__(title , balance)
        self.interestrate = interestrate

    def interestamount(self):
        interest_amount = self.interestrate * self.balance / 100
        print("The Interest amount is :" , interest_amount)
    
    def display(self):
        print("(" , self.title , "," , self.balance , "," , self.interestrate , ")")

title = input("Enter your name :")
balance = int(input("Enter your account balance :"))
account_obj = account(title , balance)
account_obj.withdrawal(int(input("Enter amount you want to withdraw :")))
account_obj.get_balance()
account_obj.deposit(int(input("Enter amount you want to deposit :")))
account_obj.get_balance()
account_obj.display()
interestrate = int(input("Enter interestrate :"))
savingsaccount_obj = savingsaccount(title , balance , interestrate)
savingsaccount_obj.interestamount()
savingsaccount_obj.display()
