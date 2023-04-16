from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 30, 'normal')


class Scoreboard(Turtle):
    def __init__(self, x_position, y_position):
        super().__init__()
        self.x_position = x_position
        self.y_position = y_position
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(x_position, y_position)
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def winner(self, x):
        self.goto(x, 0)
        self.write(f"WINNER", align=ALIGNMENT, font=('Courier', 100, 'normal'))

    def loser(self, x):
        self.goto(x, 0)
        self.write(f"LOSER", align=ALIGNMENT, font=('Courier', 100, 'normal'))

