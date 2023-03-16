from game_data import data
from art import logo, vs
import random
from replit import clear

print(logo)
points = 0


def data_chooser(given_data=data):
    choosen_data = random.choice(data)
    return choosen_data


def comparer(candidate1, candidate2, decide):
    score = 0
    #Here we take number of followers from both datas
    number1 = candidate1['follower_count']
    number2 = candidate2['follower_count']
    if number1 > number2 and decide == 'a':
        score = 1
    elif number1 < number2 and decide == 'b':
        score = 1
    elif number1 > number2 and decide == 'b':
        score = 0
    elif number1 < number2 and decide == 'a':
        score = 0
        return score


compare_b = data_chooser(data)

while True:
    compare_a = compare_b
    compare_b = data_chooser(data)
    if compare_a != compare_b:
        print(
            f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}."
        )
        print(vs)
        print(
            f"Against B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}."
        )
        decision = input("Who has more followers? Type 'A' or 'B': ").lower()
        game_score = comparer(compare_a, compare_b, decision)
        if decision != 'a' and decision != 'b':
            print(f"Sorry that was wrong. Final sore: {points}")
            break
        elif game_score == 0:
            print(f"Sorry that was wrong. Final sore: {points}")
            break
        else:
            points += 1
            clear()
            print(logo)
            print(f"You're right! Current score: {points}")
            continue
    else:
        while compare_a == compare_b:
            compare_b = data_chooser(data)
