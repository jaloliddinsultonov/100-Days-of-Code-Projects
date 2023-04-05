from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape('classic')
timmy.color('black')
timmy.pensize(10)
speed = ["fastest", "fast", 'normal', 'slow', 'slowest']
directions = [0, 90, 180, 270]
color_names = ['red', 'green', 'blue', 'orange', 'yellow', 'purple', 'pink', 'black', 'gray']

for i in range(200):
    timmy.color(random.choice(color_names))
    timmy.speed(random.choice(speed))
    timmy.forward(20)
    timmy.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()