
from abc import ABC,abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def parameter(self):
        pass


class Circle:
    pi = 3.14159
    radious = 4
    def setRadious(self,r):
        self.radious = r

    def area(self):
        self.area = self.pi * self.radious * self.radious
        return self.area
    
    def parameter(self):
        self.perimeter = 2 * self.pi * self.r
        return self.perimeter
    


class Rectangle:
    def setHeightAndWeight(self,l,w):
        self.length = l
        self.width = w    

    def area(self):
        self.area = self.length * self.width
        return self.area
    
    def perimeter(self):
        self.perimeter = 2 * self.length * self.width
        return self.perimeter
    
class Triangle:
    def setSides(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        self.area = self.a + self.b + self.c

    # def 
    

circle = Circle()
rectangle = Rectangle()
triangle = Triangle()

circle.area()
circle.parameter()
rectangle.area()
rectangle.perimeter()
# triangle.area()
triangle.perimeter()
