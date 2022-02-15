from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()


colours = ["Green", "red", "blue", "indigo", "violet", "orange", "yellow", "cyan"]
angles = [0, 90, 180, 270]
timmy.speed("fastest")
timmy.pensize(5)

for _ in range(100):

    timmy.color(random.choice(colours))
    timmy.setheading(random.choice(angles))
    timmy.forward(30)

screen.exitonclick()
