import colorgram
import turtle as t
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

brush = t.Turtle()

print(rgb_colors)