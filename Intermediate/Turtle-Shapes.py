from turtle import Turtle, Screen


def shape(the_turtle, sides, angle):
    for _ in range(sides):
        the_turtle.forward(100)
        the_turtle.right(angle)


not_a_turtle = Turtle()
for i in range(3, 11):
    shape(not_a_turtle, i, 360 / i)
screen = Screen()
screen.exitonclick()
