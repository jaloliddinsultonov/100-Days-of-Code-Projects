from turtle import Turtle, Screen
Y_COORDINATOR = -330

turtle = Turtle('square')
turtle.shapesize(stretch_len=0.5, stretch_wid=2)
turtle.speed('slowest')
turtle.penup()
turtle.goto(0, Y_COORDINATOR)


def draw_shaded_lines():
    for line in range(20):
        Y_COORDINATOR + 25
        turtle.stamp()
        turtle.goto(0, Y_COORDINATOR)
