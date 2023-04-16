from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('black')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.02

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def vertical_bounce(self):
        self.y_move *= -1

    def horizontal_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9
