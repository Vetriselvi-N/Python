# str.format()= Optional method that gives users more control when displaying output.

# we can implement str.format() in different ways
# {}---> act as a placeholder

animal="cow"
item="moon"
print("The {} jumped over the {}".format(animal,item))                        # The cow jumped over the moon
print("The {} jumped over the {}".format("cow","moon"))                       # The cow jumped over the moon
print("The {animal} jumped over the {animal}".format(animal="cow",item="moon"))      # The cow jumped over the cow
print("The {1} jumped over the {1}".format(animal,item))                      # The moon jumped over the moon


text="The {} jumped over the {}"
print(text.format(animal,item))                     # The cow jumped over the moon

# we can add padding to a String when display

name= "Bro"
print("Hello, my name is {}".format(name))          # Hello, my name is Bro
print("Hello, my name is{:5}. Nice to meet you".format(name))        # Hello, my name is Bro     . Nice to meet you
print("Hello, my name is{:<5}. Nice to meet you".format(name))       # Hello, my name is Bro     . Nice to meet you
print("Hello, my name is{:>5}. Nice to meet you".format(name))       # Hello, my name is      Bro. Nice to meet you
print("Hello, my name is{:^5}. Nice to meet you".format(name))       # Hello, my name is   Bro   . Nice to meet you

# It also suited for numbers

num=3.14159
print("The num pi is{:.3f}".format(num))          # The num pi is 3.142(rounded off)
print("The num pi is{:.2f}".format(num))          # The num pi is 3.14

num=1000
print("The num is {:3f}".format(number))          # The num is 1000.000
print("The num is {:,}".format(number))           # The num is 1,000
print("The num is {:b}".format(number))           # The num is 111110100 ( convert into binary)
print("The num is {:o}".format(number))           # The num is 1750 (convert into octal)
print("The num is {:x}".format(number))           # The num is 3E8 (convert into hexadecimal)
print("The num is {:E}".format(number))           # The num id 1.000000E+03 ( convert into scientific notation)


# Random numbers:-
# It randomly generate the range of num,lists 

import random
x=random.randint(1,6)    # generate the romdom num of a die(i.e 1-6)
print(x)                 # It will print random number each time from 1 to 6

y=random.random()        # display floating num between 0 to 1
print(y)                 # 0.8452

myList=["rock","paper","scissors"]
z= random.choice(myList)
print(z)

cards=[1,2,3,4,5,6,7,8,9,'J','Q','K','A']
random.suffle(cards)
print(cards)               # ['Q',4,'K',1,7,6,3,2,5,9,'J',8,'A']
