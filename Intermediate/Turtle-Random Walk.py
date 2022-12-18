 
from turtle import Turtle, Screen
import random
colors = ['blue', 'green', 'dark orange', 'cyan', 'pink']
directions = [0, 90, 120, 270]


def choose_path(the_turtle: Turtle):
    direction = random.choice(directions)
    the_turtle.pencolor(random.choice(colors))
    the_turtle.setheading(direction)
    the_turtle.forward(30)


tortoise = Turtle()
tortoise.pensize(5)
tortoise.speed('slow')
for _ in range(1000):
    choose_path(tortoise)

screen = Screen()
screen.exitonclick()
