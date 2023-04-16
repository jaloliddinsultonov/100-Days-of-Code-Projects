from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_coordinate, y_coordinate):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color('white')
        self.speed('fastest')
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.starting_position()

    def starting_position(self):
        return self.goto(self.x_coordinate, self.y_coordinate)

    def up(self):
        self.y_coordinate += 80
        return self.goto(self.x_coordinate, self.y_coordinate)

    def down(self):
        self.y_coordinate -= 80
        return self.goto(self.x_coordinate, self.y_coordinate)

