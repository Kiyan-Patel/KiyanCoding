import random

while True:
    user_action=input("Enter one (Rock,Paper, scissors)")
    possible_actions=["Rock, Paper, Scissors"]
    computer_action=random.choice(possible_actions)
    print(f"\n You chose {user_action}, computer chose {computer_action}.\n")

    if user_action==computer_action:
        print(f"Both players selected {user_action} Its a tie!!!!")
    elif user_action=="rock":
     if computer_action=="scissors":
        print("Rock smashes scissors.You win!!")
     else:
       print("Paper covers rock. You lose!!!")
    elif user_action=="paper":
     if computer_action=="rock":
      print("Paper covers rock.You win!!")
     else:
      print("Scissors cut paper. You lose!!!")
    elif user_action=="scissors":
     if computer_action=="papaer":
      print("Scissors cut paper.You win!!")
    else:
     print("Rock smashes scissors. You lose!!!")

    play_again=input("Play again? (y/n):")
    if play_again != "Y":
     break
       



           