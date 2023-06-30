# The Car class is a template for creating car objects.
# This Car class has two properties: color and brand.
# The color and brand properties are set in the constructor.
# and can be anything you wish, but they must be set.
# What else can you add to the Car class? Think about it like this...
# What attributes do all cars share? For instance, its reasonable to assume that 
# all cars have a Color a brand, a Steering wheel, and an Engine. 
# So, you could add a Steering wheel and an Engine to the Car class.
# Now, you can use the Car class as a template for creating anything that can be "classified" as a car.
# In Object Oriented Programming, this is called an "is-a" relationship.
# For instance, a Ford is-a car. A Toyota is-a car. A Ferrari is-a car.
# A cat "is not" a car, therefore, you can use the Car class as a template for a cat.
# In essence, the Car class is defines a car. The concept of classes in the context 
# of Object Oriented Programming is a bit more complex than this, but this is a good start.
class Car:
    def __init__(self, color, brand): # constructor
        self.color = color             # properties
        self.brand = brand             # properties

    def accelerate(self):              # method
        print("The car is accelerating.")

    def brake(self):                   # method
        print("The car is braking.")
        

if __name__ == "__main__":
    carA = Car("red", "Ford")
    carB = Car("blue", "Toyota")
    print("Car A is a " + carA.color + " " + carA.brand + ".")
    print("Car B is a " + carB.color + " " + carB.brand + ".")