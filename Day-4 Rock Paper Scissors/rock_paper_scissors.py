import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


game = True
while game:
  user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n>>> "))
  if user_choice == 0:
    print(rock)
  elif user_choice == 1:
    print(paper)
  elif user_choice == 2:
    print(scissors)
  else:
    print("Wrong number entered")

  computer_choice = random.randint(0, 2)
  print("\nComputer chose:")
  if computer_choice == 0:
    print(rock)
  elif computer_choice == 1:
    print(paper)
  elif computer_choice == 2:
    print(scissors)


  if user_choice == 0 and computer_choice == 2 or user_choice == 1 and computer_choice == 0 or user_choice == 2 and computer_choice == 1:
    print("You win")
  elif user_choice == computer_choice:
    print("Draw")
  elif user_choice == 2 and computer_choice == 0 or user_choice == 0 and computer_choice == 1 or user_choice == 1 and computer_choice == 2:
    print("You lose")

  answer = input("\nDo you want to play again? Yes/No\n>>> ")
  if answer.lower() == 'yes':
    game = True
  else:
    game = False
