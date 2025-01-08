import random

def game():
    while True:
        user_choice = input("Enter a choice (rock/paper/scissors): ").lower()
        while user_choice not in ["rock", "paper", "scissors"]:
            user_choice = input("Invalid choice. Please enter rock, paper or scissors: ").lower()

        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

        if user_choice == computer_choice:
            print(f"Both players selected {user_choice}. It's a tie!")
        elif user_choice == "rock":
            if computer_choice == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif user_choice == "paper":
            if computer_choice == "rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif user_choice == "scissors":
            if computer_choice == "paper":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")

        play_again = input("Play again? (yes/no): ").lower()
        while play_again not in ["yes", "no"]:
            play_again = input("Invalid choice. Please enter yes or no: ").lower()

        if play_again == "no":
            break

if __name__ == "__main__":
    game()
