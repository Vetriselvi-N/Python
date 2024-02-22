# function = a block of code which is executed only when it is called.

def hello():             # function declaration 
  print("hello")
  print("Have a nice day")
hello()                  # function calling 

# o/p= hello
#      Have a nice day

# function with parameters and arguments 
# function must have same no. of parameters and arguments,,otherwise it gives error


def hello(name):
  print("Hello "+ name)
  print("Have a nice day")
name= "John"
hello(name)             # Hello John.     Have a nice day
hello(name,21)          # error

# we can add'n' no. of parameters and arguments 

def hello(first_name,last_name,age):
  print("Hello "+first_name+" "+last_name)
  print("You are "+str(age)+" years old")
  print("Have a nice day")
hello("John","Mathew",21)



# return statements= Funtions send python values/objects back to the caller.
#                    TThesevalues/objects are known as the functions return value.
