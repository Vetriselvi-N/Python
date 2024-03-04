# OOP(Object Oriented Programming)= It is an instance of a class. It contains Attributes and methods 
# Attributes =is/has
# methods=actions
# class is a function of a blueprint that will describe what Attributes and methods that our distinct type of object.
# class name should be "capital"
# def__init__(self):-----> methods taht will construct objects

# file1:

class Car:                                          # class name
  def __init__(self,make,model,year,color):         # method name and arguments 
    self.make=make
    self.model=model
    self.year=year
    self.color=color
  def drive(self):
    print("This"+self.model+" is driving")
  def stop(self):
    print("This"+self.model+" is stopped")

from car import Car
car1=Car("Chevy","Corvette",2021,"Blue")
car2=Car("Ford","Mustang",2022,"Red")
print(car1.make)
print(car1.model)
print(car1.year)
print(car1.color)
print(car2.make)
print(car2.model)
print(car2.year)
print(car2.color)
car1.drive()               # This Corvette is driving
car2.stop()                # This Mustand is stopped
