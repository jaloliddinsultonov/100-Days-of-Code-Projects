from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape('classic')
timmy.color('black')

speed = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
moves = ['forward', 'backward', 'right', 'left']
color_names = ['red', 'green', 'blue', 'orange', 'yellow', 'purple', 'pink', 'black', 'gray']

number = 100
for times in range(number):
    timmy.color(random.choice(color_names))
    move = random.choice(moves)
    timmy.speed(random.choice(speed))
    if move == 'forward':
        timmy.forward(20)
    elif move == 'backward':
        timmy.backward(20)
    elif move == 'right':
        timmy.right(90)
        timmy.forward(20)
    elif move == 'left':
        timmy.left(90)
        timmy.forward(20)


screen = Screen()
screen.exitonclick()
