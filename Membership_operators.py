a=int(input("Enter your first subject's marks"))
b=int(input("Enter your second subject's marks"))
c=int(input("Enter your third subject's marks"))
d=int(input("Enter your fourth subject's marks"))
e=int(input("Enter your fifth subject's marks"))
total=a+b+c+d+e
avg=int(total/5)
Validrange=range(0,101)
if avg not in Validrange:
    print("Invalid input")
elif avg in range(91,101):
    print("Your grade is A")
elif avg in range(81,91):
    print("Your grade is B")
elif avg in range(71,81):
    print("Your grade is C")
elif avg in range(61,71):
    print("Your grade is D")
else:
    print("You are failing")
    