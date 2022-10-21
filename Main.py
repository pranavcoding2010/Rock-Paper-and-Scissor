import random
t = ["Rock","Paper","Scissor"]
computer = t[random.randint(0,2)]
player = False
while player == False:
    player = input('Rock,Paper,Scissor:')
    if player == computer :
        print("Tie")
    elif player == "Rock":
        if computer == "Paper":
            print("Computer wins")
        else :
            print("Computer lose you win")
    elif player == "Paper" :
        if computer == "Scissors" :
            print(("Computer wins"))
        else :
            print("Computer lose you win")
    elif player == "Scissors" :
        if computer == "Rock" :
            print("Computer wins")
        else :
            print("Computer lose you win")
    else :
        print("Invalid input please enter rock,paper or scissor")
    player = False
    computer = t[random.randint(0,2)]