h=float(input("Enter your height"))
w=float(input("Enter your weight"))
bmi=w/(h/100)**2
if bmi<=18.4:
    print("You are under weight")
elif bmi<=24.9:
    print("You are healthy")
elif bmi<=29.9:
    print("You are over weight")
else:
    print("You are obese")