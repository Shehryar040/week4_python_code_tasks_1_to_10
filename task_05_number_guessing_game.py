# Task 5: Number Guessing Game
import random

secret_number = random.randint(1, 100)
valid_attempts = 0
max_attempts = 7

print("Guess the secret number between 1 and 100.")

while valid_attempts < max_attempts:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a whole number. This does not use an attempt.")
        continue

    if guess < 1 or guess > 100:
        print("Your guess must be between 1 and 100. Try again.")
        continue

    valid_attempts += 1

    if guess == secret_number:
        if valid_attempts == 1:
            print("Perfect score! You guessed correctly on the first attempt.")
        else:
            print(f"Correct! You guessed the number in {valid_attempts} attempts.")
        break
    elif guess < secret_number:
        print("The secret number is higher.")
    else:
        print("The secret number is lower.")

    print(f"Attempts remaining: {max_attempts - valid_attempts}")
else:
    print("You have used all seven valid attempts.")
    print(f"The secret number was {secret_number}.")
