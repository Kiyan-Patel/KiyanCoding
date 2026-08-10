n=int(input("Enter your number"))
sum=0

temp=n
while temp>0:
    digit=temp % 10
    sum+=digit**3
    temp//=10
if sum==n:
    print("The number entered is a armstrong number")
else:
    print("The number entered is not an armstrong number")