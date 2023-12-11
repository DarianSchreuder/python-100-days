from turtle import Turtle

BALL_RADIUS = 1


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(BALL_RADIUS)
        self.color("white")
        self.speed("fastest")
        self.velocity = [10, 10]

    def move(self):
        self.forward(10)
        self.move(90)

    def bounce_wall(self):
        self.velocity = (self.velocity[0], -self.velocity[1])

    def bounce_paddle(self):
        self.velocity = (-self.velocity[0], self.velocity[1])
