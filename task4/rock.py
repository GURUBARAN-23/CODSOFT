import random

def get_user_choice():
    print("\nRock, Paper, Scissors Game")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    
    try:
        choice = int(input("Enter your choice (1-3): "))
        if choice not in [1, 2, 3]:
            print("Invalid choice. Please enter a number between 1 and 3.")
            return None
        return choice
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 1 and computer_choice == 3) or
        (user_choice == 2 and computer_choice == 1) or
        (user_choice == 3 and computer_choice == 2)
    ):
        return "You win!"
    else:
        return "You lose!"

def rock_paper_scissors_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        if user_choice is None:
            continue

        computer_choice = get_computer_choice()

        print(f"\nYour choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1

        print(f"Score - You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    rock_paper_scissors_game()
