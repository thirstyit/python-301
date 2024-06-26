# Write a script with three classes that model everyday objects.
# - Each class should have an `__init__()` method that sets at least 3 attributes
# - Include a `__str__()` method in each class that prints out the attributes
#     in a nicely formatted string.
# - Overload the `__add__()` method in one of the classes so that it's possible
#     to add attributes of two instances of that class using the `+` operator.
# - Create at least two instances of each class.
# - Once the objects are created, change some of their attribute values.
#
# Be creative. Have some fun. :)
# Using objects you can model anything you want:
# Animals, paintings, card games, sports teams, trees, people etc...

class Dog:
    def __init__(self, noise, breed, furColour) -> None:
        self.noise = noise
        self.breed = breed
        self.furColour = furColour

    def __add__(self, other):
        mix_breed = self.breed + " - " + other.breed
        return Dog(noise=self.noise, breed=mix_breed, furColour=self.furColour)
    
    def __str__(self) -> str:
        return f"Dog breed {self.breed} has {self.furColour} fur and {self.noise}."
    

d1 = Dog("barks", "Labrador", "Black")
d2 = Dog("Growls", "Alsatian", "Brown")

print(d1)
print(d2)

d3 = d1 + d2

print(d3)