# number guess
from random import randint
EASY = 10
HARD = 5

secret_number = randint(1,100)
print(secret_number)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
difficulty_choice = input("Choose a difficulty. Type 'easy or 'hard': ")
if difficulty_choice == 'easy':
    attempts = EASY
else:
    attempts = HARD
print(f"You have {attempts} attempts remaining to guess the number.")

while attempts:
    guess = int(input("Make a guess: "))
    if guess == secret_number:
        print(f"You win! You guessed my secret number with {attempts} attemptsleft.")
        break
    elif guess < secret_number:
        print("Too low.\nGuess again")
    else:
        print("Too high.\nGuess again")
    attempts -= 1
    print(f"You have {attempts} attempts remaining to guess the number")
if attempts == 0:
    print(f"You lose! You have run out of attempts. My secret number was {secret_number}.")
