from turtle import Turtle, Screen
import random

colors = ['blue', 'green', 'dark orange', 'cyan', 'pink']
tortoise = Turtle()
tortoise.speed('fastest')
screen = Screen()
screen.colormode(255)


def random_color():
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return color


for i in range(72):
    tortoise.color(random_color())
    tortoise.circle(100)
    tortoise.setheading(tortoise.heading() + 5)

screen.exitonclick()
