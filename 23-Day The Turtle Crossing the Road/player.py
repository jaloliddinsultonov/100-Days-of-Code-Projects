from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.x_coordinate = STARTING_POSITION[0]
        self.y_coordinate = STARTING_POSITION[1]
        self.penup()
        self.setheading(90)
        self.starting_position()

    # Starting position of a turtle(player)
    def starting_position(self):
        return self.goto(STARTING_POSITION)

    # Turtle(Player) goes up
    def move(self):
        self.y_coordinate += MOVE_DISTANCE
        return self.goto(self.x_coordinate, self.y_coordinate)

    # Goes back to starting position after reacher the final point, which is (x=0, y=280)
    def finish(self):
        self.x_coordinate = STARTING_POSITION[0]
        self.y_coordinate = STARTING_POSITION[1]
        return self.starting_position()

