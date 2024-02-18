# Multiple Assignment 
#In python, we can assign multiple variables and values in one single line.

a=10
b= 15.5
c="20"
print(a)     # 10
print(b)     # 15.5
print(c)     # 20

#Instead of this we can use multiple assignment method 

a,b,c= 10, 15.5,"20"
print(a,b,c)    # 10 15.5 20

a=b=c= 20
print(a,b,c)    # 20 20 20

# We can store Srting values also

a,b,c="Apple",2.4,"True"
print(a,b,c)    # Apple 2.4 True


#String Methods 

#There are many builtin functions available in python. Let us see some of the string Methods. 

name="umbrella"
print(len(name))               # length of the name
print(name.find("e"))          # Index position of the given char
print(name.capitalize())       # change the 1st char into uppercase
print(name.upper())            # change the entire name into uppercase
print(name.lower())            # change the entire name into lowercase
print(name.isdigit())          # Return bool value 
print(name.isalpha())          # Return bool value
print(name.count("e"))         # Return no of times the given is occur
print(name.replace("e","a")    # replace "e" by"a"
print(name*3)                  # 3timez the name is multiplied


#Type casting

#type()---> used to convert one data type into another 

x,y,z=1,4.5,"3"
print(x,y,z)     # 1 4.5 3

#we can typecast the above code into various types

x,y,z= 1,4.5,"3"
print(x)         #1
print(int(y))    #4
print(float(z))  #3.0
print("x is:"+ str(x))    # x is 1
