import turtle
from turtle import Turtle, Screen
import random

screen = Screen()


is_race_on = False

user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race?")
colours = ["red", "yellow", "orange", "green", "blue", "purple"]
all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-200, y=-100 + 50 * turtle_index)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 441:
            is_race_on = False
            print(f"The {turtle.pencolor()} won the race!")
            if user_bet == turtle.pencolor():
                print(f"You Guessed correct ({user_bet}) and won!")
            else:
                print(f"You guessed wrong. Guess: {user_bet}")

        turtle.forward(random.randint(0, 10))


# if user_bet == winner:
#     print("You win!")
# else:
#     print("you loose")
screen.exitonclick()
