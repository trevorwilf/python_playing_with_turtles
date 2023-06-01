from turtle import Turtle, Screen, colormode
from random import randint

def create_polygon(sides):
    degreeturn = 360/i
    mturtle.pencolor(randint(0,255), randint(0,255), randint(0,255))
    mturtle.pendown()
    for j in range(i):
        mturtle.forward(200)
        mturtle.right(degreeturn)

mscreen = Screen()
mturtle = Turtle()

#set turtle defaults and starting position
mturtle.shape("turtle")
mturtle.color("red")
mturtle.penup()
mturtle.left(90)
mturtle.forward(470)
mturtle.left(90)
mturtle.forward(100)
mturtle.left(180)
colormode(255)

for i in range(3,30):
    create_polygon(i)


mscreen.exitonclick()