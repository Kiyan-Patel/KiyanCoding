actualcost=float(input("Enter the actual price"))
salecost=float(input("Enter the salecost"))
if salecost<actualcost:
    Amount=actualcost-salecost
    print("Total profit is equal to",Amount)
else:
    print("No profit ")