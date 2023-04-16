from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

Y_COORDINATOR = -350

screen = Screen()
screen.setup(width=1500, height=700)
screen.bgcolor('green')
screen.title("Ping Pong")
screen.tracer(1, 0)

# these for creating shaded lines in a screen
turtle = Turtle('square')
turtle.color('white')
turtle.shapesize(stretch_len=0.3, stretch_wid=2)
turtle.speed('slowest')
turtle.penup()
turtle.goto(0, Y_COORDINATOR)

for i in range(13):
    turtle.stamp()
    turtle.goto(0, Y_COORDINATOR)
    Y_COORDINATOR += 60

# Creating two paddles and a ball
paddle_1 = Paddle(-700, 0)
paddle_2 = Paddle(700, 0)
ball = Ball()
score_1 = Scoreboard(-60, 250)
score_2 = Scoreboard(60, 250)

screen.listen()
screen.onkey(paddle_1.up, "w")
screen.onkey(paddle_1.down, "s")
screen.onkey(paddle_2.up, "Up")
screen.onkey(paddle_2.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision ball with wall
    if ball.ycor() > 330 or ball.ycor() < -330:
        # needs to bounce
        ball.vertical_bounce()

    if ball.distance(paddle_2) < 50 and ball.xcor() > 680 or ball.distance(paddle_1) < 50 and ball.xcor() < -680:
        time.sleep(ball.move_speed)
        ball.horizontal_bounce()

    if ball.xcor() > 730:
        score_1.increase_score()
        ball.home()
        ball.move_speed = 0.05
        ball.horizontal_bounce()
        ball.move()

    elif ball.xcor() < -730:
        score_2.increase_score()
        ball.home()
        ball.move_speed = 0.05
        ball.horizontal_bounce()
        ball.move()

    if score_1.score == 5:
        score_1.winner(x=-300)
        score_2.loser(x=300)
        game_is_on = False

    elif score_2.score == 5:
        score_2.winner(x=300)
        score_1.loser(x=-300)
        game_is_on = False


screen.exitonclick()