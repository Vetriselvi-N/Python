# Nested Function calls= Function calls inside other Function calls
#                        Innermost Function calls are resolved first
#                        Returned value is used as arguments for the next outer Function.

num= int(input("Enter a whole number:"))
num= float(num)
num= abs(num)
num= round(num)
print(num)

# Instead of this no. of line of codes,we use

print(round(abs(float(input("Enter a whole number:")))))




# Variables scope= The region that a variable is recognized.
#                  A variable is only available from inside the region it is created called local scope
#                  A Global and Local scope versions of a variable can be created.


name="Code"   # Global scope(Available inside and outside Function)
def display_name():
  name="Bro"    # Local scope(Available only inside the Function)
  print(name)
display_name()
print(name)               

# O/P:Bro
#     Code

# If we doesn't give Local variable then the Function returns Global variable as the "name"

name="Code"   
def display_name(): 
  print(name)
display_name()
print(name)  

#O/P:Code
#    Code

# Python follows "LEGB" rule
# L= Local
# E= Enclosing
# G= Global
# B= Built-in
