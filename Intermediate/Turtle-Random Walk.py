from turtle import Turtle, Screen
import random
screen = Screen()
screen.colormode(255)
directions = [0, 90, 120, 270]


def random_color():
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return color


def choose_path(the_turtle: Turtle):
    direction = random.choice(directions)
    the_turtle.color(random_color())
    the_turtle.setheading(direction)
    the_turtle.forward(30)


tortoise = Turtle()
tortoise.pensize(5)
tortoise.speed('slow')
for _ in range(1000):
    choose_path(tortoise)

screen.exitonclick()
