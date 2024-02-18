# Variables are the container for a value. We can assign any type of values like int, float, String, bool.
# To store the String value we use wither single('') or double("") quotes.

name= "Python"
print(python)

name="Python"
print(name + "is good")       # Pythonis good
print(name + " " +"is good")  # Python is good

name1="Python"
name2="is good"
print(name1+name2)   # Python is good

#type() ------> It is a function which is used to check the data type

age="50"    # String
age=50      # int


age= 20
age+=1
print("my age is:"+ age)      # error Because, we cannot concatenate str with any other data type
print("my age is:"+str(age))  # my age is 20

# We can also use float or bool to concatenate with String using type() method.
