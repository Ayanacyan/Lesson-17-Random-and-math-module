import random

while True:
    user_action=input("Choose 1 rock, paper, or scissors:")
    possible_actions=('rock','paper','scissors')
    computer_action= random.choice(possible_actions)
    print("You chose", user_action, "The computer chose",computer_action)

    if user_action==computer_action:
        print("Both players selected", user_action," it's a tie!")

    elif user_action=='rock':
        if computer_action=='scissors':
            print("Rock smashes scissors, You Win")
        else:
            print("Paper covers rock, Computer Wins!")
    
    elif user_action=='scissors':
        if computer_action=='paper':
            print("Scissors cut the Paper, You Win!")
        else:
            print("Rock smashed your Scissors, Computer Wins")

    else:
        if computer_action=="rock":
            print("Paper covers rock, You Win!")

        else:
            print("Scissors cut the paper, Computer Wins!")
    
    play_again= input("Play Again? y/n")
    if play_again!="y":
        break