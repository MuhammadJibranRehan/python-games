import random

def rock_paper_scissor():
    choices = ["rock", "paper", "scissors"]
    computer_score = 0
    user_score = 0

    while True:
        user_choice = input("Enter your choice (rock, paper, scissors) or 'q' to quit: ").lower()

        if user_choice == 'q':
            break

        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"\nComputer chose {computer_choice}.")

        if user_choice == computer_choice:
            print(f"Both players selected {user_choice}. It's a tie!")
        elif user_choice == "rock":
            if computer_choice == "scissors":
                print("Rock smashes scissors! You win this round.")
                user_score += 1
            else:
                print("Paper covers rock! You lose this round.")
                computer_score += 1
        elif user_choice == "paper":
            if computer_choice == "rock":
                print("Paper covers rock! You win this round.")
                user_score += 1
            else:
                print("Scissors cuts paper! You lose this round.")
                computer_score += 1
        elif user_choice == "scissors":
            if computer_choice == "paper":
                print("Scissors cuts paper! You win this round.")
                user_score += 1
            else:
                print("Rock smashes scissors! You lose this round.")
                computer_score += 1

        print(f"\nScore - You: {user_score}, Computer: {computer_score}\n")

    print("Game over. Final score:")
    print(f"You: {user_score}, Computer: {computer_score}")

rock_paper_scissor()
