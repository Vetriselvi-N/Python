# Class variables
# The variable inside the constructor is called instance variable
# Class variable is devlared inside the class but outside the constructor

class Car:
  wheels=4          # class variable
  def __init__(self,make,model,year,color):
    self.make= make      # instance variable
    self.model=model     # instance variable
    self.year=year       # instance variable
    self.color=color     # instance variable
from car import Car
car1=Car("Chevy","corvette",2021,"blue")
car2=Car("Ford","Mustang",2022,"red")
print(car1.wheels)                    # 4
print(car2.wheels)                    # 4

# We can change class variables by using this method 

car1.wheels=2
print(car1.wheels)                   # 2
print(car2.wheels)                   # 4

# Another way to access a class variables

print(Car.wheels)                    # 4

# we want to change a class variable through class

Car.wheels=2
print(car1.wheels)                  # 2
print(car2.wheels)                  # 2
