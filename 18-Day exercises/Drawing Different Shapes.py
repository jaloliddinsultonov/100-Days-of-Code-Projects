from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape('classic')
timmy.color('black')

color_names = ['red', 'green', 'blue', 'orange', 'yellow', 'purple', 'pink', 'black', 'gray']

timmy.up()
timmy.goto(-30, 300)
timmy.down()
number = 3
while number <= 8:
    color = random.choice(color_names)
    for i in range(number):
        timmy.color(color)
        degree = 360 / number
        timmy.forward(100)
        timmy.right(degree)

    number += 1


screen = Screen()
screen.exitonclick()