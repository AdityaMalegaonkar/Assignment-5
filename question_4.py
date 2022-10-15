# Assignment - 5

# 4. Implement a Banking Account

class account:
    def __init__(self , title , balance):
        self.title = title
        self.balance = balance

    def display(self):
        return f"({self.title} , {self.balance})"

class savingsaccount(account):
    def __init__(self , title , balance , interestrate):
        super().__init__(title , balance)
        self.interestrate = interestrate

    def display(self):
        return f"({self.title} , {self.balance} , {self.interestrate})"

title = input("Enter your name :")
balance = int(input("Enter your account balance :"))
interestrate = int(input("Enter interestrate :"))
account_obj = account(title , balance)
print(account_obj.display())
savingsaccount_obj = savingsaccount(title , balance , interestrate)
print(savingsaccount_obj.display())
