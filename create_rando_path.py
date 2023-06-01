import random
from turtle import Turtle, Screen, colormode
from random import randint

directions = [0, 90, 180, 270]
mscreen = Screen()
mturtle = Turtle()

#set turtle defaults and starting position
mturtle.shape("turtle")
mturtle.color("red")
mturtle.pensize(10)
mturtle.speed("fastest")
colormode(255)

def get_random_direction():
    dir = randint(0,3)
    if (dir == 0):
        mturtle.left(90)
    elif (dir == 1):
        mturtle.left(180)
    elif (dir == 2):
        mturtle.left(270)

def get_random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    #mturtle.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    color_tuple = (r,g, b)
    return(color_tuple)

for _ in range(1, 400):
    #get_random_direction()
    mturtle.setheading(random.choice(directions))
    #get_random_color()
    mturtle.pencolor(get_random_color())
    mturtle.forward(30)
    #mturtle.forward(randint(10,30))

mscreen.exitonclick()