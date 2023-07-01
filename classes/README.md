# Classes  


Chuck Sailer  
July 1st, 2023

In object-oriented programming, a class is a blueprint for creating objects. It's a user-defined data type, which defines the properties (data) and methods (functions) that an object can have.

Here are some specifics:

1. **Properties (also known as attributes or fields)**: These are the variables that belong to a class. They represent the state or quality of an object. For example, a "Car" class might have properties like color, brand, model, speed, etc.

2. **Methods**: These are functions that belong to a class. They represent the behavior of an object and can manipulate the properties of the class. For example, the "Car" class might have methods like accelerate(), brake(), turn(), etc.

3. **Constructor**: This is a special method that is used to initialize a new object of the class. It gets called when an object of that class is created.

4. **Inheritance**: A class can inherit the properties and methods of another class. This is a key feature of object-oriented programming that promotes code reuse and the design principle of "is-a" relationship. For example, a "Truck" class might inherit from the "Car" class, because a truck "is a" type of car.

Here's a basic example in Python:

```python
class Car:
    def __init__(self, color, brand): # constructor
        self.color = color             # properties
        self.brand = brand             # properties

    def accelerate(self):              # method
        print("The car is accelerating.")

    def brake(self):                   # method
        print("The car is braking.")
```

This defines a Car class, which has properties (color, brand) and methods (accelerate, brake). You can create an object of this class and call its methods like this:

```python
my_car = Car("red", "Toyota") # create a Car object
my_car.accelerate()           # call the accelerate method
my_car.brake()                # call the brake method
```

## self
In Python, self is a convention used in instance methods (accelerate, brake) to refer to the object on which the method is being called. It's always the first parameter in the definition of class instance methods. It allows you to access the instance's attributes and other methods. For example, lets add a `describe()` method to the Car class:

```python
class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def describe(self):
        return f'This is a {self.color} {self.brand}.'
```

In this example, ```self``` is used in the ```__init__``` method (also known as a constructor) to define the Color and Brand attributes of an instance of the Car class. ```self.color = color``` means "assign the value of the color parameter to the color attribute of this instance of Car".

In the ```describe()``` method, ```self``` is used to access these attributes to provide a description of the car.

So when you create an instance of the Car class:

```python
my_car = Car('red', 'Toyota')
print(my_car.describe())
```

It would output:
```python
This is a red Toyota.
```

It's important to note that self is **NOT** a keyword in Python, and you could technically name ```self``` anything you want. However, it is a very strong convention in Python and other developers will expect you to use self, so it's best to stick with it unless you have a very good reason not to.


Classes are one of the fundamental concepts in object-oriented programming and they form the basis for complex software systems by encapsulating data and functionality into reusable and modular components.