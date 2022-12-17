import random
from turtle import Turtle, Screen
import random

colors = ['blue', 'green', 'dark orange', 'firebrick']


def shape(the_turtle, sides, angle):
    for _ in range(sides):
        the_turtle.forward(100)
        the_turtle.right(angle)


not_a_turtle = Turtle()
for i in range(3, 11):
    not_a_turtle.pencolor(colors[i % 4])
    shape(not_a_turtle, i, 360 / i)
screen = Screen()
screen.exitonclick()
