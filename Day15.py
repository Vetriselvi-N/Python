# file detection:

import os
path="C:\\users\\desktop\\folder"
if os.path.exists(path):
  print("The location exists")
  if os.path.isfile(path):
    print("That is a file")
  elif os.path.isdir(path):
    print("That is a directory")
else:
  print("The location doesn't exist")


# Read a file:
# No need to manually close the file. It automatically close the file after reading.

with open("text.txt") as file:
  print(file.read())
print(file.closed)

# If we give file name as wrong, it displays FileNotFoundError.
# To avoid this, we go for exceptional handling.

try:
  with open("text.txt") as file:
    print(file.read())
except FileNotFoundError:
  print("That file was not found")


# write a file :

text= "Yoooooo \n This is some text \n Have a good one \n"
with open("test.txt",'w') as file:
  file.write(text)

# If the text value changes, it overrides the new one
# We can also append the values

text="Have a nice day! see ya"
with open("test.txt",'a') as file:
  file.write(text)
