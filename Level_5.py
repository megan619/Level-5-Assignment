#Create two functions
# get_player_choice: This function should prompt the player, convert the response to lowercase, 
# validate the choice, and return the result.
def get_player_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
    return choice
# determine_winner: This function should compare the two choices and return "win", "loss", or "tie".
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "win"
    else:
        return "loss"
    
# Welcome the user to the rock paper scissors game & ask how many rounds they would like to play. 
# Ensure that the number of rounds is odd.
import random
print("Welcome to Rock Paper Scissors!")
rounds = int(input("How many rounds would you like to play? "))
while rounds % 2 == 0:
    print("Please enter an odd number of rounds.")
    rounds = int(input("How many rounds would you like to play? ")) 

# Keep track of the number of wins and losses for both the player and the computer. 
player_wins = 0
computer_wins = 0
for i in range(rounds):
    player_choice = get_player_choice()
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_choice}")
    
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):  
        print("You win this round!")
        player_wins += 1
    else:
        print("Computer wins this round!")
        computer_wins += 1

# Determine winner and print results
if player_wins > computer_wins:
    print("Congratulations! You won the game!")
elif computer_wins > player_wins:
    print("Sorry, the computer won the game.")
else:
    print("The game ended in a tie.")


