
from turtle import Turtle, Screen

my_turtle = Turtle()
my_screen = Screen()

def move_forwards():
    my_turtle.forward(10)

def move_backwards():
    my_turtle.backward(10)

def move_clockwise():
    cur_heading = my_turtle.heading()
    my_turtle.setheading(cur_heading - 5)

def move_cclockwise():
    cur_heading = my_turtle.heading()
    my_turtle.setheading(cur_heading + 5)

def clear_screen():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()

my_screen.listen()
my_screen.onkey(key="w", fun=move_forwards)
my_screen.onkey(key="s", fun=move_backwards)
my_screen.onkey(key="a", fun=move_clockwise)
my_screen.onkey(key="d", fun=move_cclockwise)
my_screen.onkey(key="c", fun=clear_screen)

my_screen.exitonclick()