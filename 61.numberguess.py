import random

# Computer picks a random number between 1 and 100
number_to_guess = random.randint(1, 100)
attempts = 0

print("I'm thinking of a number between 1 and 100. Can you guess it?")

while True:
    try:
        user_guess = int(input("Enter your guess: "))
        attempts += 1
        
        if user_guess < 1 or user_guess > 100:
            print("Please guess a number within the range 1-100.")
            continue
        
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break
    except ValueError:
        print("Invalid input. Please enter a number.")
