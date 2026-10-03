try:
   a=int(input("Enter the number"))
   print("What is the value", a)
except ValueError as ex:
   print("What you have entered is incorrect", ex)