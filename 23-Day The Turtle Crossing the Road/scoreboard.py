from turtle import Turtle
ALIGNMENT = 'left'
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color('black')
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    # Appears 'GAME OVER' word in the center of the screen
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align='center', font=FONT)

    # Increases level of a turtle by 1 and shows it on the screen
    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)
