# Lists: used to stire multiple items in a single variable
# Each item in a list is consider as a element.
# it is changeable 

food=["pizza","hamburger","hotdog","spaghetti","pudding"]
print(food)
print(food[4])      # pudding
food[0]=["Sushi"]   # changes "pizza" as "Sushi"
print(food[0])      # Sushi
for x in food:
  print(x)


food= ["pizza","hamburger","hotdog","spaghetti","pudding"]
food.append("ice cream")
food.remove("hot dog")
food.pop()
food.insert(0,"cake")     # it will insert cake in 0th Index and pizza in 1st index
food.sort()               # it will sort the food based on Alphabet
for x in food:
  print(x)

food.clear()              # clear all the elements in list.
print(x)




# 2D lists= a list of lists

drinks=["Coffee","Soda","Tea"]
dinner=["pizza","hamburger","hotdog"]
dessert=["cake","ice cream"]
food=[drinks,dinner,dessert] 
print(food)                  #[["Coffee","Soda","Tea"],["pizza","hamburger","hotdog"],["cake","ice cream"]]
print(food[0][0])            # Coffee
print(food[1][2])            # hotdog
print(food[2][1])            # ice cream



# Tuplea= Collection of Data which is ordered and unchangeable. 
# Used to group together related data


student=("John",21,"male")
print(student.count("John"))        # 1
print(student.index("male"))        # 2
for x in student:
  print(x)
if "male" in student:
  print("Hi Bro")
