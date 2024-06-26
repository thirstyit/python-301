# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        print("Area: " + str(area))

    def perimeter(self):
        perimeter = 2 * self.length + 2 * self.width
        print("Perimeter: " + str(perimeter))


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = self.radius * self.radius * 3.14 
        print("Area: " + str(area))

    def circumference(self):
        circumference = 2 * 3.14 * self.radius
        print("Circumference: " + str(circumference))



c = Circle(2)
r = Rectangle(2,2)

c.area()
c.circumference()

r.area()
r.perimeter()
