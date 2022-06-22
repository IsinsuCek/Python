import random

def rps_game(user_choice):

    
    actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(actions)
    print(f"You chose {user_choice}\nComputer chose {computer_action}")

    if user_choice == computer_action:
        print(f"Both players selected {user_choice}, it's a tie!")

    elif user_choice == 'rock':
        if computer_action == 'scissors':
            print(f"{user_choice} smashes {computer_action}. You won!")
        else:
            print(f"{computer_action} covers {user_choice}. You lost!")

    elif user_choice == "paper":
        if computer_action == "rock":
            print(f"{user_choice} covers {computer_action}. You won!")
        else:
            print(f"{computer_action} cuts {user_choice}. You lost!")

    elif user_choice == "scissors":
        if computer_action == "paper":
            print(f"{user_choice} cuts {computer_action}. You won!")
        else:
            print(f"{computer_action} smashes {user_choice}. You lost.")

user_input = input("Enter a choice (rock, paper, scissors): ")
rps_game(user_input)

