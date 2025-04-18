
import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to Guess the Number game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        user_guess = input("Take a guess: ")

        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        attempts += 1

        if user_guess < number_to_guess:
            print("Too low!")
        elif user_guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break

number_guessing_game()
