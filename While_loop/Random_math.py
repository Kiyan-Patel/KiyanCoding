import random
playing=True
num=str(random.randint(0,9))

print("You will have to guess a number 0,9, choose one number each.")
print("The game ends when you have one hero")

while playing:
    guess= input("Give me your best guess /n")
    if num==guess:
     print("You guessed right!!")
     print("The number was ", num)

     break
    else:
     print("oops try again")

    