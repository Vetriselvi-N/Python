# if statements
# block of code that will execute if it's condition is true


age= int(input("How old are you?:"))
if agee==100:
  print("You are century old")
elif age>=18:
  print("You are an adult")
elif age<0:
  print("You are not born yet")
else:
  print("You are a child")




# logical operators(and,or,not)
# used to check two or more statements is true or not



if (temp>=0 and temp<=30):
  print("Temperature is good today")
  print("Go outside")
elif(temp>30 or temp<=50):
  print("Temperature is bad today")
  print("Stay inside")
elif(not(temp>0)):
  print("It's cold today")


# while loops
# A statement that will execute it's block of code,as long as it's conditions remains true.


while 1==1:
  print("I'm stuck")    # loop goes infinitely

name=""
while(len(name==0)):
  name=input("Enter the name:")
print("Hello"+name)



# for loops
# A statement that will execute it's block of code, a limited amount of time.
# while loop= unlimited 
# for loop= limited


for i in range(10):   # It will print from 0 to 9
  print(i)

for i in range(50,100):    # It will print from 50 to 99
  print(i)

for i in range(50,100,2):     # It will print from 50 to 100 with the step of 2
  print(i)

for i in range("Python"):
  print(i)

for seconds in range(10,0,-1):
  print(seconds)
  time.sleep(1)
print("Happy New Year")


# Nested loops
# The "inner loop" will finished all of it's iterations before finishing one iteration of the outer loop.


rows= int(input("Enter the no.of rows:"))
colunms= int(input("Enter the no.of columns:"))
symbol= input("Enter the symbol to use:")
for i in range(rows):
  for j in range(columns):
    print(symbol,end="")
  print()
