import random
user_wins = 0
computer_wins = 0
options = ["rock", "paper","scissor"]
while True:
    user_choice=input("enter your choice : ROCK / PAPER / SCISSOR or Q to quit: ").lower()
    if user_choice == "q":
        break
    if user_choice not in options:
        continue
    random_num = random.randint(0,2)
    computer_choice= options[random_num]
    print("computer picked" , computer_choice + "." )

    if user_choice=="rock" and computer_choice=="scissor":
        print("you win")
        user_wins+=1
    elif user_choice=="paper" and computer_choice == "rock":
        print(" you win")
        user_wins+=1
    
    elif user_choice=="scissor" and computer_choice =="paper":
        print("you win")
        user_wins+=1
    elif user_choice==computer_choice:
        print("its a tie")
    else:
        print("you lost")
        computer_wins+=1
print("you won", user_wins, "times.")
    
print("computer won", computer_wins , "times")
print("---GAME OVER---!")