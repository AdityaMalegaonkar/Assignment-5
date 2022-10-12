# Assignment - 5

# 1. Square Numbers and Return Their Sum

class point:
    def __init__(self):
        self.x = x
        self.y = y
        self.z = z

    def sqsum(self):
        sq_x = self.x ** 2
        sq_y = self.y ** 2
        sq_z = self.z ** 2
        self.sq_sum = sq_x + sq_y + sq_z

    def __str__(self):
        return f"Sum of squares of these three numbers is : {self.sq_sum}"

x = int(input("Enter first number :"))
y = int(input("Enter second number :"))
z = int(input("Enter third number :"))
point_obj = point()
point_obj.sqsum()
print(point_obj)