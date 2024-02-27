# Exception handling = events detected during exection that interrupt the flow of a program.
# To avoid the ZeroDivisionError, ValueError,and many more,,,we use try and except method 

try: 
  numerator = int(input("Enter numerator:"))
  denominator= int(input("Enter denominator:"))
  result=numerator/denominator 
except ZeroDivisionError as e:
  print(e)                         # It print the type of error
  print("You can't divide by zero")
except ValueError as e:
  print(e)
  print("Enter only numbers")
except Exception as e:
  print(e)
  print("Something went wrong")
else:
  print(result)
finally:                          # This keyword will always execute 
  print("This will always execute")
