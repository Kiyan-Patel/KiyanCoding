#string=input("Please enter your own word")
#char=input("Please enter your letter")
#i=0
#count=0
#while (i<len(string)):

 #   if(string[i]==char):
  #      count=count+1
   #     i=i+1
    #print("The letter",char,"has occurred",count )

#Take input of a word

string = input("Please enter your own word : ")

#take input of a character

char = input("Please enter your own Character : ")

i = 0

count = 0

#loop will to find the occurence of character

while(i < len(string)): #string operation

 if(string[i] == char): #condition 1
  count = count + 1
  i = i + 1
  print("The total Number of Times ", char, " has Occurred = " , count)
