# To map real world scenrios, we use OPPS
# Class is blue print for creating objects

# ---- Class : ----
# class Student:
#     name = "Deepak Ghimire"

# ----- Object : -----
# obj = Student()
# print(obj.name)

# ---- Constructor (__int__): ----
# class Student:
#     name = "Deepak Ghimire"
#     def __init__(self):# self means inself, point to itself (object)
#         print("Creating new student....")
#         print(self)

# obj = Student()
# print(obj.name)

# ---- Attribute : ----
# Class and Instance Attributes
# class.attr
# obj.attr
# obj attr have higher attribute

# ---- Methods: ----
# class Student:
#     def __init__(self,name):
#         print("Taking name ....")
#         self.name = name

#     def getname(self):
#         print(self.name)

# obj = Student("Deepak")
# obj.getname()


# ---- Practice: ----
# class Student:
#     def __init__(self,name,marks1,marks2,marks3):
#         self.name = name
#         self.marks1 = marks1
#         self.marks2 = marks1
#         self.marks3 = marks1

#     def average(self):
#         sum = self.marks1 + self.marks2 + self.marks3
#         average = sum/3
#         print(average)

# stdd = Student("sereynn",92,88,79)
# stdd.average()

# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
        

#     def average(self):
#         sum = 0
#         for mark in self.marks:
#             sum += mark
#         print(f"Hello {self.name} your average is : {sum/3}")
# stdd = Student("sereynn",[90,99,100])
# stdd.average()


# --- 10 Practice Questions: ----
# -- 1. Create a Class for a Student, Create a Student class with attributes: name, age, and grade. Create multiple objects and print their details.
# class Student:
#     def __init__(self,name,faculty,age,grade):
#         self.name = name
#         self.faculty = faculty
#         self.age = age
#         self.grade = grade

#     def getDetails(self):
#         print(self.name)
#         print(self.grade)
#         print(self.age)
#         print(self.faculty)

# stdd1 = Student("Oggy","CS",18,"Bachelors")
# stdd1.getDetails()

# -- 2. Bank Account Class, Create a BankAccount class with methods to deposit, withdraw, and check_balance. Prevent withdrawal if balance is insufficient.
class Bank:
    moeny = 0

    def deposit(self, depositMoney):
        money = amount


    def withdraw(self, withdrawMoney):
        if(money != 0):
            if(money >= withdrawMoney):
                money -= withdrawMoney
            else:
                print("Ammount unsuffecent")
        else:
                print("Ammount unsuffecent")

    
    def checkbalance(self):
         print("amount : ", money)

    

newUser = Bank()
isRun = True
while(isRun):
    try:
        operation = int(input("Enter 1 for deposit\nEnter 2 for withdraw\nEnter 3 for checking money\n:"))
        if(operation == 1):
             try:
                dmoney = int(input("Enter a amount of money you want to add:"))
                newUser.deposit(dmoney)
             except Exception as e:
                print("plz enter a valid number")

        # elif(operation == 2):
            
             
    except Exception as e:
              print("Please enter a valid operation")
              
                   
        

 