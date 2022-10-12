# Assignment - 5

# 4. Implement a Banking Account

class account:
    def __init__(self , title = None , balance = 0):
        self.title = "Ashish"
        self.balance = 5000

    def display(self):
        print("(" , self.title , "," , self.balance , ")")

class savingsaccount(account):
    def __init__(self , title = None , balance = 0 , interestrate = 0):
        super().__init__(title , balance)
        self.interestrate = 5

    def display(self):
        print("(" , self.title , "," , self.balance , "," , self.interestrate , ")")

account_obj = account()
account_obj.display()
savingsaccount_obj = savingsaccount()
savingsaccount_obj.display()