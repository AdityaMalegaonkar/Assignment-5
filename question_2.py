#  Assignment - 5

# 2. Implement a Calculator Class

class calculator:

    def __init__(self):
        self.num1 = int(input("Enter first number :"))
        self.num2 = int(input("Enter second number :"))

    def add(self):
        self.addition = self.num1 + self.num2

    def subtract(self):
        self.subtraction = self.num1 - self.num2

    def multiply(self):
        self.multiplication = self.num1 * self.num2

    def divide(self):
        self.division = self.num2 / self.num1

    def __str__(self):
        return f"\n Addition : {self.addition} \n Subtraction : {self.subtraction} \n Multiplication : {self.multiplication} \n Division : {self.division}"

calculator_obj = calculator()
calculator_obj.add()
calculator_obj.subtract()
calculator_obj.multiply()
calculator_obj.divide()
print(calculator_obj)