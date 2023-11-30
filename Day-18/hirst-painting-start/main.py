# import colorgram
import turtle as t
from random import choice

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))

rgb_colors = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]

brush = t.Turtle()
brush.speed("fastest")
brush.penup()
t.hideturtle()
t.colormode(255)

x_pos = 0
y_pos = 0
for x in range(12):
    brush.setposition(x_pos - 400, y_pos - 400)
    x_pos = 0
    x_pos += x
    for y in range(12):
        y_pos += y
        t.delay(70)
        brush.dot(20, choice(rgb_colors))

        brush.forward(50)

screen = t.Screen()
screen.exitonclick()
