# Base class
class Vehicle:
    def move(self):
        print("The vehicle is moving")

# Subclass Car
class Car(Vehicle):
    def move(self):
        print("driving on the road")

# Subclass Bicycle
class Bicycle(Vehicle):
    def move(self):
        print("pedaling on the road")

# Demonstrating polymorphism
vehicles = [Car(), Bicycle()]

for v in vehicles:
    v.move()
