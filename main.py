# This is my rock paper scissors game
# I want to add visuals to it
import random

options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)

running = True

# running is a boolean variable
while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"PLayer: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "Scissors":
        print("YOU WIN!")
    elif player == "paper" and computer == "rock":
        print("YOU WIN!")
    elif player == "scissors" and computer == "paper":
        print("YOU WIN!")
    else:
        print("YOU LOSE!")

    play_again = input("Play again? (y/n): ").lower()
    if not play_again == "y":
        running = False

print("Thanks for playing!")
