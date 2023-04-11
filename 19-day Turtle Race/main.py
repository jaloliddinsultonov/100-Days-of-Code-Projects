from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=500)
user_guess = screen.textinput(title='Make a guess', prompt="Which turtle will win the "
                                                           "race?\n-Red\n-Orange\n-Yellow\n-Green\n-Blue\n-Purple"
                                                           "\nEnter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
is_right = True
y_position = -180

joey = Turtle('turtle')
rachel = Turtle('turtle')
phoebe = Turtle('turtle')
ross = Turtle('turtle')
monica = Turtle('turtle')
chandler = Turtle('turtle')

turtles = [joey, rachel, phoebe, ross, monica, chandler]

joey.color(colors[0])
rachel.color(colors[1])
phoebe.color(colors[2])
ross.color(colors[3])
monica.color(colors[4])
chandler.color(colors[5])

for trtl in turtles:
    trtl.penup()
    trtl.goto(x=-230, y=y_position)
    y_position += 50

while is_right:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_right = False
            winner = turtle.pencolor()
            if winner == user_guess.lower():
                print(f"You won! {winner} turtle won the race!")
            else:
                print(f"You lose! {winner.title()} turtle won the race!")

        turtle.forward(random.randint(0, 10))

screen.exitonclick()
