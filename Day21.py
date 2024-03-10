# method overriding= ability of an object Oriented Programming language to allow a child class to provide a specific implementation of a method that us already provided by one of its parents.

class Animal():
  def eat(self):
    print("This animal is eating ")
class Rabbit(Animal):
  def eat(self):                               # method that overrides the parent class method
    print("This rabbit is eating a carrot")
rabbit=Rabbit()
rabbit.eat()                                  # This rabbit is eating a carrot


# method chaining= calling multiple methods sequentially 
#                  Each call performs an action on the same object and returns self


class Car:
  def turn_on(self):
    print("You start the engine")
    return self
  def drive(self):
    print("You drive the car")
    return self
  def brake(self):
    print("You step on the brake")
    return self
  def turn_off(self):
    print("You turn off the engine")
    return self
car=car()
car.turn_on().drive()                 # You start the engine  You drive the car
car.brake().turn_off()                # You step on the brake  You turn off the engine
car.turn_on()\.drive()\.brake()\.turn_off()    # You start the engine
                                               # You drive the car
                                               # You step on the brake
                                               # You turn off the engine
