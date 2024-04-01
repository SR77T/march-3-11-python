# Create a class Circle .with an attribute radius. Create two objects of circle c1 and c2. Add the radius of the 
# circles and print the result.
# # Do the above task using a method and then a magic method
# 

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def total_radius(self, other):  # method
        return self.radius + other.radius

    def __add__(self, other):  # method
        return self.radius + other.radius
    
    def __gt__(self, other):
        return self.radius > other.radius
    
    def __lt__(self, other):
        return self.radius < other.radius


c1 = Circle(5)
c2 = Circle(10)
total_radius = c1.radius + c2.radius
print(total_radius)  # 15  SImple

print(c1.total_radius(c2))  # using method
print(c1 + c2)  # 15
print(c1 > c2)  #false
print(c1 < c2)  # True
 
# Operator overloading is also one of the features of Python OOP
# In python most of the operators invoke the magic methods
# Magic methods are the methods with double underscores in each side
# Magic methods are also called dunder methods


a = 1
b = 2
print(a + b)
result = a.__add__(b)
print(result)

print(b.__sub__(a))

a = [1, 2, 3]
iter_a = iter(a)
# print(next(iter_a))
print(iter_a.__next__())


class A:
    def __str__(self):
        return "Object of A"

    def __add__(self, other):
        return self.v + other.v


a = A()  # obj
print(a.__str__())
print(str(a))