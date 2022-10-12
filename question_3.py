# Assignment - 5

# 3. Implement the Complete Student Class

class student:
    
    def set_name(self , name):
        self.__name = name
    def get_name(self):
        return f"Name : {self.__name}"
    
    def set_rollnumber(self , rollnumber):
        self.__rollnumber = rollnumber
    def get_rollnumber(self):
        return f"Roll Number : {self.__rollnumber}"

student_obj = student()
student_obj.set_name(input("Enter your name :"))
student_obj.set_rollnumber(input("Enter your roll number :"))
print(student_obj.get_name())
print(student_obj.get_rollnumber())