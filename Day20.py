# Multilevel Inheritance = when a child class inherits another child class

class Organism:            # grand parent class
  alive=True
class Animal(Organism):        # Parent class
  def eat(self):
    print("This animal is eating")
class Dog(Animal):
  def bark(self):
    print("This dog is barking")
dog=Dog()
print(dog.alive)          # True
dog.eat()                 # This animal is eating
dog.bark()                # This dog is barking


# Multiple Inheritance= when a child class is derived from more than one parent class.

class Prey:
  def flee(self):
    print("This animal flees")
class Predator:
  def hunt(self):
    print("This animal is hunting")
class Rabbit(Prey):
  pass
class Hawk(Predator):
  pass
class Fish(Prey,Predator):
  pass
rabbit=Rabbit()
hawk=Hawk()
fish=Fish()
rabbit.flee()            # This animal flees
hawk.hunt()              # This animal is hunting
fish.flee()              # This animal flees
fish.hunt()              # This animal is hunting 
