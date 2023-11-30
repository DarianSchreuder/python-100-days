import turtle
from turtle import Turtle, Screen

turtle.delay(10)
tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(50)


def move_backward():
    tim.backward(50)


def turn_right():
    new_heading = tim.heading() - 90
    tim.setheading(new_heading)
    tim.forward(50)


def turn_left():
    new_heading = tim.heading() + 90
    tim.setheading(new_heading)
    tim.forward(50)


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_right, "d")
screen.onkey(turn_left, "a")
screen.exitonclick()
