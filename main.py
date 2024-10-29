# - Pick a random number between 1 and 100.
# - Set attempts to 0 and maximum attempts to 5.
# - Prompt the player to guess the number.
# - Check if the guess is too low, too high, or correct.
# - If incorrect, give a hint (too low or too high) and increase attempts by 1.
# - If correct, congratulate the player and end the game.
# - If attempts reach the max and no correct guess, reveal the correct number and end the game.

import random

number = random.randint(1, 10)
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    guess = int(input("Guess a number: "))

    if guess > number:
        print("Too High! Try Again")
    elif guess < number:
        print("Too Low! Try Again")
    else:
        print(f"Congrats! The number {guess} is correct!")
        break

    attempts += 1
    print(f"Attempts: {attempts}")

    if attempts == max_attempts:
        print(f"Max attempts reached! The correct number was {number}.")