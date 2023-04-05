from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape('turtle')
timmy.color('red', 'blue')

for i in range(15):
    timmy.forward(10)
    timmy.up()
    timmy.forward(10)
    timmy.down()


screen = Screen()
screen.exitonclick()