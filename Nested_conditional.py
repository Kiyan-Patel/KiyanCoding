a=input("Do you have a medical case(y/n)").strip().upper()
if a=="Y":
    print("You are allowed")
else:
    attn=int(input("Enter your attendence"))
    if attn>=75:
        print("Allowed")
    else:
        print("Not allowed")