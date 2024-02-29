# copy a file

# copyfile()= It copies content of a file
# copy() = copyfile()+permission mode+destination can be a directory 
# copy2()= copy()+copies meta data(files creation and modification times)

import shuttle
shutil.copyfile('test.txt','c:\\users\\desktop\\copy.txt') # it copy only text file
shutil.copy('test.txt','c:\\users\\desktop\\copy.txt') # it copies the folder
shutil.copy2('test.txt','c:\\users\\desktop\\copy.txt') # it copies the folder with text files


# move a file

import os 
source='test.txt'
destination="c:\\users\\desktop\\test.txt"
try:
  if os.path.exists(destination):
    print("Already a file is there")
  else:
    os.replace(source,destination)
    print(source+" was moved")
except FileNotFoundError:
  print(source+" was moved")

# delete a file

import os
path=" test.txt"
try:
  os.remove(path)
except FileNotFoundError:           # for text file
  print("That file was not found")
except PermissionError:             # for folder/directory 
  print("You do not have permission")
except OSError:                     # folder which contains files
  print("You cannot delete that using this function")
else:
  print(path+" was deleted")


#another meyhid to delete a folder/directory 
import os
path= os.rmdir(path)
print("folder deleted successfully")

#another meyhid to delete a folder which contains some files

import os
import shutil 
path=shutil.rmtree(path)   # it delete everything in the folder


# modules= a file containing python code, it may contain functions,classes etc
#          used with modular programming, which is to separate a progress into parts.

#file 1(messages.py)
def hello():
  print("Hello! Have a nice day")
def bye():
  print(" Bye! Have a wonderful time")
# file 2(main.py)
import messages 
messages.hello()
messages.bye()

import messages as msg
msg.hello()
msg.bye()

# for small no.of module

from messages import hello,bye
hello()
bye()

# for large no.of modules

from messages import *
hello()
bye()

# python has bunch of modules. To display the modules, we use

help(modules)      # It displays list of all the modules available.
