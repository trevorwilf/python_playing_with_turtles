import random
from turtle import Turtle, Screen, colormode
from random import randint
import colorgram

color_pallete = colorgram.extract('Ellipticine.png', 150)
print(color_pallete)

color_pallete_list = []
for i in range(0, len(color_pallete)):
    cur_col = color_pallete[i].rgb
    cur_tup = (cur_col.r, cur_col.g, cur_col.b)
    #try to filter out whites
    if (cur_tup[0] + cur_tup[1] + cur_tup[2] < 230 * 3):
        color_pallete_list.append(cur_tup)

# setup turtle
mscreen = Screen()
mturtle = Turtle()

mturtle.shape("turtle")
mturtle.color("red")
colormode(255)
mturtle.speed("fastest")

# set starting location
mturtle.penup()
mturtle.goto(-mscreen.window_width()/4, mscreen.window_height()/4)

gridsize = [10, 15]
move = 40
direction = 1

for i in range(0, gridsize[0]):
    for j in range(0, gridsize[1]):
        mturtle.dot(20, random.choice(color_pallete_list))
        mturtle.forward(move)

    mturtle.back(move)
    mturtle.setheading(270)
    mturtle.forward(move)

    if direction > 0:
        mturtle.setheading(180)
    else:
        mturtle.setheading(0)

    direction = direction * -1

mturtle.hideturtle()
mscreen.exitonclick()