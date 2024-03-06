# Inheritance = It has parent- child class 

class Animal:
  alive=True     # class variable
  def eat(self):
    print("This animal is eating")
  def sleep(self):
    print("This animal is sleeping")
class Rabbit(Animal):
  pass              # placeholder
class Fish(Animal):
  pass
class Hawk(Animal):
  pass
rabbits=Rabbit()          # object that stores the class
fish=Fish()
hawk=Hawk()
print(Rabbit.alive)      # True
Fish.eat()               # This animal is eating
Hawk.sleep()             # This animal is sleeping 

# we can create multiple methods for each class


class Animal:
  alive=True     # class variable
  def eat(self):
    print("This animal is eating")
  def slumber(self):
    print("This animal is sleeping")
class Rabbit(Animal):
  def run(self):
    print("This rabbit is running")
class Fish(Animal):
  def swim(self):
    print("This fish is swimming")
class Hawk(Animal):
  def fly(self):
    print("This hawk is flying")

rabbit=Rabbit()          # object that stores the class
fish=Fish()
hawk=Hawk()
Rabbit.run()            # This rabbit is running
Fish.swim()             # This Fish is swimming
Hawk.fly()              # This Hawk is flying
