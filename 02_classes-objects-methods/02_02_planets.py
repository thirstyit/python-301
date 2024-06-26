# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

class Planet():
    def __init__(self, name, fromSun, howManyMoons):
        self.name = name
        self.fromSun = fromSun
        self.howManyMoons = howManyMoons

    def oneMoreMoon(self):
        self.howManyMoons += 1

    def __str__(self) -> str:
        return f"Planet {self.name} is {self.fromSun} from Sun and has {self.howManyMoons} moons."
    


m = Planet("Mercury", 1, 2)
e = Planet("Earth", 3, 1)
print(m)
print(e)