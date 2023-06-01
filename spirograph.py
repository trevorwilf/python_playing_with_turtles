from turtle import Turtle, Screen, colormode
from random import randint

mscreen = Screen()
mturtle = Turtle()

def get_random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    #mturtle.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    color_tuple = (r,g, b)
    return(color_tuple)

#set turtle defaults and starting position
mturtle.shape("turtle")
mturtle.color("red")
colormode(255)
mturtle.speed("fastest")

num_of_circles = 80
radius = 200

for _ in range(0,num_of_circles):
    mturtle.pencolor(get_random_color())
    mturtle.circle(radius)
    mturtle.left(360/num_of_circles)




mscreen.exitonclick()