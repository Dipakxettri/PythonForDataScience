# When to Use Abstract Classes ??..
# Abstract classes are useful when you want to:
# Define a common interface for all subclasses (e.g., all animals must have a sound()).
# Enforce implementation of certain methods in child classes.
# Provide shared functionality (concrete methods) while still requiring subclasses to implement specific behavior.


# Abstract methods are methods that are defined in an abstract class but do not have an implementation. They serve as a blueprint for the subclasses, ensuring that they provide their own implementation.


from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod # this method should be implimented in its child class otherwise throws an error....
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("Hau Hau") 


# animal = Animal()
# animal.sound()


# dog = Dog()
# dog.sound()