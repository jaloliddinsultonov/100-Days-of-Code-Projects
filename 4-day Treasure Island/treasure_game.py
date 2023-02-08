# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 19:47:21 2023

@author: Jaloliddin
"""
print("""
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
""")

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
answer_1 = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n>>>")
if answer_1.lower() == "right":
    print("You fell into a hole. Game over.")
else:
    answer_2 = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n>>>")
    if answer_2.lower() == "swim":
        print("You are attacked by trout. Game over.")
    else:
        answer_3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n>>>")
        if answer_3.lower() == "red":
            print("You are burned by fire. Game over.")
        elif answer_3.lower() == 'blue':
            print("You are eaten by beasts. Game over.")
        elif answer_3.lower() == "yellow":
            print("You win. The Treasure is yours now!!! Hurrayyy!!!!")
        else:
            print("You misclicked. Game over")
        