# Build on your freeform exercise from the previous section.
# Create child classes of two of the existing classes. Create a child class
# of one of the child classes so that the hierarchy is at least three levels.
#
# Build these classes out step-by-step like you did in the previous exercises.
# Use your notebook to brainstorm ideas and scribble down ideas.
#
# If you cannot think of a way to build on your freeform exercise,
# you can start with a new class from scratch.
# Try to make up your own example for this exercise, but if you are stuck,
# you could start working on the following:
#
# - A `Vehicle()` parent class, with `Truck()` and `Motorcycle()` child classes.
# - A `Restaurant()` parent class, with `Gourmet()` and `FastFood()` child classes.

class Vehicle():
    def __init__(self, engine, model, year):
        self.year = year
        self.engine = engine
        self.model = model
        self.speed = 0

    def faster(self):
        self.speed +=10

    def __str__(self) -> str:
        return f"Vehicle year {self.year} engine {self.engine} model {self.model} speed {self.speed}."

class Car(Vehicle):
    def __init__(self, engine, model, year):
        super().__init__(engine, model, year)
        self.wheels = 4
        self.passengers = 1

    def more_passengers(self):
        self.passengers += 1

    def faster(self):
        self.speed +=15

    def __str__(self) -> str:
        return super().__str__() + f"Car with Wheels {self.wheels} passengers {self.passengers}"


class Motorbike(Car):
    def __init__(self, engine, model, year):
        super().__init__(engine, model, year)
        self.wheels = 2
        self.passengers = 1

    def faster(self):
        self.speed +=20

    def __str__(self) -> str:
        return super().__str__() + f"Mbike Wheels {self.wheels} passengers {self.passengers}"
    
v = Vehicle("electric", "Tesla", 2009)
print(v)

c = Car("Diesel", "Volkswagen", 2011)
print(c)

m = Motorbike("Petrol", "Harley", 2001)
print(m)


c.faster()
print(c)

m.faster()
print(m)
