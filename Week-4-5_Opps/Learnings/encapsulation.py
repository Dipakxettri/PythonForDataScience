# class Student:
#     def __init__(self,name,age):
#         self.__name = name
#         self.age = age

# student = Student("deepak",18)
# print(student.name) # error because name is private
# print(student.age)

# Access Specifiers:
# public, private, protected


# -- Getter and Setter Methods: --
class Customer:
    def __init__(self):
        self.__salary = 2000

    # Getter
    def getSalary(self):
        print(self.__salary)

    # Setter
    def setSalary(self,amt):
        if(amt > 0):
            self.__salary = amt
        else:
            print("plz enter valid salary")

customer = Customer()
customer.setSalary(1200000)
customer.getSalary()




