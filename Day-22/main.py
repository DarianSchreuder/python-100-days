from ball import Ball
from turtle import Screen
from paddle import Paddle
from time import sleep
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.tracer(0)

screen_height = screen.window_height() / 2
screen_width = int(screen.window_width() / 2)
l_screenwidth = -screen_width + 20
r_screenwidth = screen_width - 20
left_paddle = Paddle((l_screenwidth, 0))
right_paddle = Paddle((r_screenwidth, 0))

ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() > screen_height - 20 or ball.ycor() < -screen_height + 20:
        ball.bounce_wall()

    if ball.distance(left_paddle) < 50 and ball.xcor() < -screen_width + 40 or ball.distance(
            right_paddle) < 50 and ball.xcor() > screen_width - 40:
        ball.bounce_paddle()

    if ball.xcor() > screen_width:
        ball.reset_position()
        scoreboard.l_score_inc()
    elif ball.xcor() < -screen_width:
        ball.reset_position()
        scoreboard.r_score_inc()
screen.exitonclick()
