import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

eddie = Turtle()
eddie.shape("classic")
eddie.speed('fastest')
eddie.hideturtle()
y_coordinate = -250

color_list = [(211, 154, 98), (53, 107, 131), (177, 78, 33), (198, 142, 35), (116, 155, 171), (124, 79, 98),
              (123, 175, 157), (226, 197, 130), (190, 88, 109), (12, 50, 64), (56, 39, 19), (41, 168, 128),
              (50, 126, 121), (199, 123, 143), (166, 21, 30), (224, 93, 79), (243, 163, 161), (38, 32, 34), (3, 25, 25),
              (80, 147, 169), (161, 26, 22), (21, 78, 90), (234, 167, 171), (171, 206, 190), (103, 127, 156),
              (165, 202, 210)]

eddie.penup()
eddie.setx(-250)
eddie.sety(-250)

for j in range(10):
    for i in range(10):
        eddie.color(random.choice(color_list))
        eddie.dot(20)
        eddie.forward(50)

    y_coordinate += 50
    eddie.setx(-250)
    eddie.sety(y_coordinate)

screen = Screen()
screen.exitonclick()
