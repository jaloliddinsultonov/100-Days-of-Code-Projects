import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shapesize(8, 8, outline = 1)
timmy.hideturtle()
turtle.colormode(255)
timmy.speed('fastest')


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    arr = (r, g, b)
    return arr


for i in range(120):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.right(3)
    timmy.forward(3)


screen = Screen()
screen.exitonclick()

