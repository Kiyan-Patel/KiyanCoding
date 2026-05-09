Amount=int(input("Enter the amount"))

#Calculating the number of notes
note1=Amount//100
note2=(Amount%100)//50
note3=((Amount%100)%50)//10

print("The number of 100 dollar notes are",note1)
print("The number of 50 dollar notes are",note2)
print("The number of 10 dollar notes are",note3)