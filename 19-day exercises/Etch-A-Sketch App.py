from turtle import Turtle, Screen

ed = Turtle()
screen = Screen()


def forward():
    ed.forward(10)


def backward():
    ed.backward(10)


def right():
    ed.right(10)


def left():
    ed.left(10)


def clear():
    ed.reset()
    

screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key='s', fun=backward)
screen.onkey(key='d', fun=right)
screen.onkey(key='a', fun=left)
screen.onkey(key='c', fun=clear)
screen.exitonclick()
