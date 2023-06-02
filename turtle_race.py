from turtle import Turtle, Screen
from random import randint

# setup the screen info
my_screen = Screen()
my_screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color red, orange, yellow, green, blue, purple: ")

turtle_list = []
for i in range(6):
    clone_turtle = Turtle(shape="turtle")
    clone_turtle.penup()
    clone_turtle.color(colors[i])
    clone_turtle.goto(-200, (-100 + (40 * i)))
    turtle_list.append(clone_turtle)



if user_bet:
    is_race_on =True

while is_race_on:
    for turtle in turtle_list:
        travel_speed = randint(0,15)
        turtle.forward(travel_speed)
        if turtle.position()[0] > 200:
            winner = turtle.color()[0]
            is_race_on = False

if (winner == user_bet.lower()):
    print("You Win!")
    print(f"The winning turtle is {winner}")
else:
    print("You lose :(")
    print(f"The winning turtle is {winner}")



my_screen.exitonclick()