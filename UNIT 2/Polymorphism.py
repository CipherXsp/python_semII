#create a base class vehicle with a method mover() and two subclasses Car and bicycle. override the move() method in both subclasses. the car should print "driving on the road" and the #bicycle should print "pedaling on the road" demonstrate polymorphism by calling the move() method on both objects

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


