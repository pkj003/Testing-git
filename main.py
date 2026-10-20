import random


def play_round() -> None:
    secret_number = random.randint(1, 100)
    attempts = 7

    print("\nI'm thinking of a number from 1 to 100.")
    print(f"You have {attempts} guesses. Enter 'q' to quit.")

    for attempt in range(1, attempts + 1):
        guess_text = input(f"Guess {attempt}/{attempts}: ").strip()

        if guess_text.lower() == "q":
            print("Thanks for playing!")
            return

        try:
            guess = int(guess_text)
        except ValueError:
            print("Please enter a whole number.")
            continue

        if not 1 <= guess <= 100:
            print("Your guess must be between 1 and 100.")
        elif guess == secret_number:
            print(f"You got it in {attempt} {'guess' if attempt == 1 else 'guesses'}!")
            return
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

    print(f"Out of guesses! The number was {secret_number}.")


def main() -> None:
    print("Welcome to Guess the Number!")
    while True:
        play_round()
        if input("\nPlay again? (y/n): ").strip().lower() != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()