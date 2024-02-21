# Dictionaries= changeable, unordered collection of unique" key:value" pairs
# Fast because they use hashing, it allows us to access a value quickly.

capitals={"USA":"Washington DC",
          "India":"New Delhi",
          "China":"Beijing",
          "Russia":"Modcow"}
for key,value in capitals.items():
  print(key,value)
print(capitals["Russia"])          # Moscow
print(capitals["Germany"])         # error
print(capitals.get("Germany"))     # None
print(capitals.keys())             # only print the keys
print(capitals.values())           # only print the valies
print(capitals items())            # print both keys and value


capitals.update({"Germany":"Berlin"})       #add new Kay,value pair
capitals.update({"USA":"Lasvegas"})         # update the value of "USA"
capitals.pop("China")                       # remove the key,value pair of China
for key,value in capitals.items():
  print(key,value)


capitals.clear()     # clear all the key,value pairs
for key,value in capitals.items():
  print(key,value)





# Index operator[] = gives access to a sequences of elements (str,list,tuples)

name="Hello python"
if(name[0].islower()):
  name= name.capitalize()
print(name)                     # Hello python 
