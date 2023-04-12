from turtle import Turtle
import random

colors = ["red", "orange", "yellow", "lime", "green", "aqua", "blue", "purple", "pink", "magenta", "turquoise", "gold"]
shapes = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color('red')
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        self.color(random.choice(colors))
        self.shape(random.choice(shapes))
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
