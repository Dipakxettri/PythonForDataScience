# Polymorphism:
# => Polymorphism means "many forms"

# Types :
# 2. Compile-time Polymorphism
# 1. Runtime Polymorphism (Overriding)

# Compile-time Polymorphism(Over Loading):
# class Animal:
#      def sound(self):
#           print("Generic sound")

# class Dog(Animal):
#      def sound(self):
#           print("Hau Hau")

# dog = Dog()
# dog.sound()

# Runtime Polymorphism (Overriding):
class Add:
    def add(self, *args):
        if len(args) == 2:
            a,b = args
            print(a * b)

        elif len(args) == 4:
            a,b,c,d = args
            print(a * b * c * d)

        else:
            print("Unsuppoted number of arguments")

add = Add()
add.add(2,2)  
add.add(2,2,2,2)   