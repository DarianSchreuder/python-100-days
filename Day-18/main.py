import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


directions = [0, 90, 180, 270]

tim.speed("fastest")
tim.pensize(1)


def spiral(size):
    angle = 0
    size *= 2
    for _ in range(36):
        tim.color(random_color())
        tim.circle(size)
        tim.setheading(angle)
        angle += 10


spiral(20)
spiral(30)
spiral(100)
spiral(150)
spiral(200)
screen = t.Screen()
