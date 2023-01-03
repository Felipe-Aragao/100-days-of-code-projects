from colors import colors_list
from random import choice
import turtle as t

HOME_X = -200
home_y = -200

turtle = t.Turtle()
turtle.penup()
turtle.hideturtle()
turtle.speed(0)
turtle.goto(HOME_X, home_y)

screen = t.Screen()
screen.colormode(255)

for row in range(10):
    for dot in range(10):
        turtle.dot(20, choice(colors_list))
        turtle.forward(50)
    home_y += 50
    turtle.goto(HOME_X, home_y)

screen.exitonclick()
