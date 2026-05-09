print("Enter your 4 subject marks")
Math=int(input("Math:"))
English=int(input("English:"))
History=int(input("HIstory:"))
Science=int(input("Science:"))

#Lets calculate the percentage of marks
Sum=Math+English+History+Science
print("The sum of all subjects is ",Sum)
perc=(Sum/400)*100
print("Percentage is ",perc)