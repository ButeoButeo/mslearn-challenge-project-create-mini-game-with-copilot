import random

def rock_paper_scissors():
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    player_choice = None

    print("Welcome to Rock, Paper, Scissors!")
    print("Choose your option: rock, paper, or scissors")

    while player_choice not in options:
        player_choice = input("Enter your choice: ").lower()

    print(f"Computer chose: {computer_choice}")
    print(f"You chose: {player_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

def main():
    play_again = 'y'
    while play_again.lower() == 'y':
        rock_paper_scissors()
        play_again = input("Do you want to play again? (y/n): ")

if __name__ == "__main__":
    main()