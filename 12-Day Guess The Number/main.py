#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random 

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
computer_guess = random.randint(1, 100)
mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if mode == "hard":
  attempt = 5
elif mode == "easy":
  attempt = 10

while attempt > 0:
  print(f"You have {attempt} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
  if guess > computer_guess:
    print("Too high.")
    attempt -= 1
  elif guess < computer_guess:
    print("Too low")
    attempt -= 1
  elif guess == computer_guess:
    print(f"You got it! The answer was {computer_guess}.")
    break
  if attempt == 0:
    print("You've run out of guesses, you lose.")
    
