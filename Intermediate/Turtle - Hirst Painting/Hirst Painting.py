from turtle import Turtle, Screen
import colorgram, random

colors = colorgram.extract('hirst.jpeg', 40)
colors = [(i.rgb.r, i.rgb.g, i.rgb.b) for i in colors]
colors.remove((252, 251, 244))
colors.remove((254, 247, 252))  # Background colors
colors.remove((241, 253, 246))
colors.remove((245, 248, 253))

screen = Screen()
screen.colormode(255)
my_lil_turtle = Turtle()
my_lil_turtle.speed('fastest')
my_lil_turtle.penup()
my_lil_turtle.setpos(-225, -200)  # Optimal coordinates obtained after trial and error using pos()
current_pos = my_lil_turtle.pos()  # Deprecated but kept for demonstration purposes
for _ in range(10):
    for __ in range(10):
        my_lil_turtle.dot(20, random.choice(colors))
        my_lil_turtle.forward(50)
    my_lil_turtle.setpos(current_pos[0], current_pos[1] + (50*(_ + 1)))


screen.exitonclick()
