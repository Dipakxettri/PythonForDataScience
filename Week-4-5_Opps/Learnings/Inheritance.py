# Types of Inheritance:
# Single Inheritance: A child class inherits from a single parent class.
# Multiple Inheritance: A child class inherits from more than one parent class.
# Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another class.
# Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
# Hybrid Inheritance: A combination of two or more types of inheritance.


# Single Inheritance
# class Animal:
#     def __init__(self):
#         print("the animal class")
#     def setName(self,name):
#         self.name = name

# class Dog(Animal):
#     def sound():
#         print("Hau Hau")
#     def getName (self):
#         print(self.name)
    
# # animal = Animal()
# dog = Dog()
# dog.setName("Tommy")
# dog.getName()


# ---- Problms : ----
# -- 1. Create a class Person with attributes name and age.
# Create a subclass Employee that inherits from Person and adds an attribute salary.
# Create an object of Employee and print all attributes. --
# Ans =>
# class Person:
#     name = "Oggy"
#     age = 18

# class Employee(Person):
#     salary = 1000

# empy = Employee()
# print(empy.name)
# print(empy.age) 
# print(empy.salary) 

# -- 2. Create a base class Vehicle with method description() that prints "This is a vehicle".
# Create a subclass Car that overrides the description() method. --
# class Vehicle:
#     def description(self):
#         print("This is a vehicle")

# class Car(Vehicle):
#     def description(self):
#         print("This is a Car")

# v = Vehicle()
# v.description()
# c = Car()
# c.description()

# -- 3. Create a class Shape with a constructor that sets a color attribute.
# Create a subclass Rectangle that uses super() to inherit the color and adds length and width. --
# class Shape:
#     def __init__(self,color):
#         self.color = color

# class Rectange(Shape):
#     def __init__(self, color, length, width):
#         self.length = length
#         self.width = width
#         super().__init__(color)

# rectange = Rectange("red",12,14)
# print(rectange.color)
# print(rectange.length)
# print(rectange.width)

# -- Q no 4. Multilevel Inheritance
# Problem:
# Create three classes:
# LivingThing
# Animal (inherits from LivingThing)
# Human (inherits from Animal)
# Each class should print a message in its constructor. Create a Human object and observe the constructor chain. --
# class LivingThings:
#     def __init__(self):
#         print("this is Living Things")

# class Animal(LivingThings):
#     def __init__(self):
#         print("this is Animal class")
#         super().__init__()

# class Human(Animal):
#     def __init__(self):
#         print("this is Human class")
#         super().__init__()

# human = Human()

# -- Q no 5. Hierarchical Inheritance
# Problem:
# Create a base class Bird.
# Create two subclasses: Parrot and Sparrow, both inheriting from Bird.
# Add unique methods to each subclass. Demonstrate that both share methods from Bird. --

# class Bird :
#     def __init__(self):
#         print("Hello Bird")

# class Parrot(Bird):
#     def __init__(self,sound):
#         self.sound = sound
#         super().__init__()

# class Sparrow(Bird):
#     def __init__(self,sound):
#         self.sound = sound
#         super().__init__()

# bird = Bird()
# parrot = Parrot("Cheu cheu")
# print(parrot.sound)
# sparrow = Sparrow("dj dj")
# print(sparrow.sound)

# -- Q no 6. Multiple Inheritance
# Problem:
# Create two classes: Writer and Painter, each with a method show_profession().
# Create a class Artist that inherits from both.
# Demonstrate that Artist has access to both methods. --

# class Writer:
#     def show_profession(self):
#         print("complited half of the writing")

# class Painter:
#     def show_profession(self):
#         print("complited half painting")

# class Artist(Writer,Painter):
#     pass

# artist = Artist()
# artist.show_profession()
# print(Artist.__mro__)
# =>
# Method Resolution Order (MRO) Behaviour in the following code.
# Python looks for show_profession() in:
# Artist → doesn't exist
# Writer → found ✅
# Stops here. Painter is ignored.
# That’s why even though Painter also defines show_profession(), it’s never called.






