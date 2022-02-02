# simple rock paper scissors game
# might be an easier way to have the game print the full word rather than the letter
# any suggestions are welcome and appreciated! :)

import random

def play_game():
    user = input("Type 'r' for rock, 'p' for paper, and 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        if computer == 'r':
            computer = 'rock'
            print(f"Computer picked {computer}. You tie!")
        elif computer == 's':
            computer = 'scissors'
            print(f"Computer picked {computer}. You tie!")
        elif computer == 'p':
            computer = 'paper'
            print(f"Computer picked {computer}. You tie!")

    elif is_win(user, computer):
        if computer == 'r':
            computer = 'rock'
        elif computer == 'p':
            computer = 'paper'
        elif computer == 's':
            computer = 'scissors'
        print(f"The computer picked {computer}. You win!!")

    else:
        if computer == 'r':
            computer = 'rock'
        elif computer == 'p':
            computer = 'paper'
        elif computer == 's':
            computer = 'scissors'
        print(f"The computer picked {computer}. You lose.. :(")


def is_win(player,opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True


play_game()