import random

choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

print("=== Rock-Paper-Scissors ===")

while True:
    user = input("rock, paper, or scissors? (q to quit): ")

    if user == "q":
        break

    if user != "rock" and user != "paper" and user != "scissors":
        print("Invalid input. Try again.")
        continue

    computer = random.choice(choices)
    print("Computer chose:", computer)

    if user == computer:
        print("Tie!")
    elif user == "rock" and computer == "scissors":
        print("You win!")
        user_score = user_score + 1
    elif user == "paper" and computer == "rock":
        print("You win!")
        user_score = user_score + 1
    elif user == "scissors" and computer == "paper":
        print("You win!")
        user_score = user_score + 1
    else:
        print("Computer wins!")
        computer_score = computer_score + 1

print("Final score - You:", user_score, "Computer:", computer_score)