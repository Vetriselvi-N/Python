# args= Parameter taht will pack all arguments into a tuple.
#       Useful so that a function can accept a varying amount of arguments.


def add(num1,num2):
  sum=num1+num2
  return sum
print(add(1,2))        # 3
print(add(1,2,3))      # error 

#Instead of giving seperate parameters, we can give " *args "

def add(*args):          # args is not as much as important, "*" is important 
  sum=0
  for i in args:
    sum+=I
  return sum
print(add(1,2,3,4))        # 10

# It works as tuple, so we cannot change the tuple values.So, we first convert tuple into list

def add(*stuff):
  sum=0
  stuff= list(stuff) # convert tuple into list
  stuff[0]=0
  for i in stuff:
    sum+=i
  return sum
print(add(1,2,3,4))       # 10


# **kwargs= Parameters that will pack all arguments into a dictionary.
#           Useful so that a function can accept a varying amount of keyword arguments.

def hello(first,last):
  print("Hello"+first+" "+last)
hello(first="Bro",middle="Dude",last="Code")        # error

# Instead of this ,we can use "**kwargs"

def hello(**kwargs):
  print("Hello"+kwargs["first"]+" "+kwargs["last"])
hello(first="Bro",middle="Dude",last="Code")         # Hello Bro Code


def hello(**kwargs):
  print("Hello")
  for key,value in kwargs.items():
    print(value)
hello(first="Bro",middle="Dude",last="Code")

# O/p= Hello
#      Bro
#      Dude
#      Code
