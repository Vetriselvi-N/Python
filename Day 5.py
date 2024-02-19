# Loop control statements = Change a loops execution from it's normal sequence

# break = Used to terminate the loop entirely 
# continue = Skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder


# break:

name=input("Enter your name:")
if name!="" :
  break


# continue:

phone_number = "123-456-7890"
for i in phone_number:
  if i=="-":
    continue
  print(i,end="")


# pass:

for i in range(1,21):
  if(i==13):
    pass
  else:
    print(i)
