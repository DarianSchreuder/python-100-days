from snake import Snake
from turtle import Screen
from food import Food
from score import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen_width = screen.window_width()
screen_height = screen.window_height()
width = screen_width / 2
height = screen_height / 2

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        score.increase_score()
        food.refresh()
        snake.extend()

    if snake.head.xcor() > width or snake.head.xcor() < -width or snake.head.ycor() > height or snake.head.ycor() < -height:
        game_is_on = False
        score.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
screen.exitonclick()
