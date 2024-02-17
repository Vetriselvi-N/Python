# user input:

name=input("What is your name?:")
print(name)      # What is your name?: John  and o/p is John

#like string, we cannot get int/float data directly from the user. So, we use typecasting. 

age=int(input("How old are you?:")
height=float(input(How tall are you?:")
print(age)       # How old are you?:21. and o/p is 21
print(height)    # How tall are you?:136.4 and the o/p is 136.4



#Math functions:

pi=3.14
print(round(pi))         # 3
print(math.ceil(pi))          # 4
print(math.floor(pi))         # 3
print(abs(pi))                # 3.14
print(pow(3,2))               # 9
print(math.sqrt(25))          # 5

a,b,c= 10,2,53
print(max())                  # 53
print(min())                  # 2

#Slicing:
#Used to create a substring by extracting elements from other string
#indexing[] or slicing()
#[start:stop:step]
#indexing[]


name="Python is good"
first_name=name[0:6]
last_name=name[10:]
mid_name=name[7:9]
franky_name=name[0::2]
reverse_name=name[::-1]
print(first_name)         # Python
print(last_name)          # good
print(mid_name)           # is
print(franky_name)        # Pto sgo
print(reverse_name)       # doog si nohtyP

# slicing----> used to find the website names


website1= https://google.com
website2=https://Wikimedia.com
slice(7,-4)
print(website1)      # google
print(website2)      # wikipedia
