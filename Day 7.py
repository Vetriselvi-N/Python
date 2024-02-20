# Sets= Collection which is unordered, unindexed
# It has no duplicate values

utensils={"fork","spoon","knife"}
for x in utensils:
  print(x)           # since it is an unsorted and unindexed, it print different order each time of execution

# since sets doesn't allow duplicate elements, it displays only once when the elements, are repeated.

utensils={"fork","spoon","knife","knife"}
for x in utensils:
  print(x)           # it print knife only once

# sets have some built-in functions

utensils={"fork","spoon","knife"}
print(utensils.add("napkin"))       # add "napkin" at the end of the elements 
print(utensils.remove("fork"))      # remove "fork" from the set
print(utensils. clear())            # clear all the elements 


utensils={"fork","spoon","knife"}
dishes={"bowl","plate","cup","knife"}
print(utensils.update(dishes))      # add dishes to the utensils 
print(dishes.update (utensils))     # add utensils to the dishes 
print(dinner_table=utensils.union(dishes))    # combines both utensils and dishes
print(utensils.difference(dishes))        # displays what utensils have that doesn't dishes have
print(dishes.difference(utensils))        # displays what dishes have that doesn't utensils have
print(utensils. intersection(dishes))     # displays common item that present in both utensils and dishes 
