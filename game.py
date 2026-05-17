import random
import time

# Generate random number
number = random.randint(1, 200)


# Function to display introduction
def intro():
    print("\n===== NUMBER GUESSING GAME =====")
    name = input("Enter your name: ")

    print(f"\nWelcome {name}!")
    print("I am thinking of a number between 1 and 200.")
    time.sleep(0.5)
    print("You have 6 attempts to guess it. Good luck!\n")


# Function to play the game
def play_game():

    guesses_taken = 0

    while guesses_taken < 6:

        try:
            guess = int(input("Enter your guess (1-200): "))

            # Check range
            if guess < 1 or guess > 200:
                print("Please enter a number between 1 and 200.\n")
                continue

            guesses_taken += 1

            if guess < number:
                print("Too low!\n")

            elif guess > number:
                print("Too high!\n")

            else:
                print(f"Correct! You guessed it in {guesses_taken} attempts.\n")
                return True

        except ValueError:
            print("Invalid input! Please enter a valid number.\n")

    print(f"Game Over! The correct number was {number}\n")
    return False


# Main loop (play again feature)
while True:

    intro()
    play_game()

    again = input("Do you want to play again? (yes/no): ").lower()

    if again != "yes" and again != "y":
        print("\nThanks for playing!")
        break