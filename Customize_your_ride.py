print("select your ride")
print("1.bike")
print("2.car")
choice=int(input("Enter your choice"))
if choice==1:
    print("What type of bike")
    print("1.superbike")
    print("2.Cruiser")
    choice2=int(input("Enter your choice 2"))
    if choice2==1:
        print("Your have chosen a superbike")
    else:
        print("YOu have chosen a cruiser")
elif choice==2:
    print("What type of car")
    print("1.sedan")
    print("2.SUV")
    choice3=int(input("Enter your choice 3"))
    if choice3==1:
        print("Your have chosen a sedan")
    else:
        print("YOu have chosen a SUV")
else:
    print("WRONG CHOICE")