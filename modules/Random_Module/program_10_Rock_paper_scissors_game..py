# Rock paper scissors game.
import random

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)

user = input("Enter rock/paper/scissors : ")

print("Computer :", computer)

if user == computer:
    print("Match Draw")

elif user == "rock" and computer == "scissors":
    print("You Win")

elif user == "paper" and computer == "rock":
    print("You Win")

elif user == "scissors" and computer == "paper":
    print("You Win")

else:
    print("Computer Wins")