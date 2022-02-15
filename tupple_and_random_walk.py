import turtle as t
from turtle import Screen
import random

t.colormode(255)
timmy = t.Turtle()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    ran_c = (r, g, b)
    return ran_c


angles = [0, 90, 180, 270]
timmy.speed("fastest")
timmy.pensize(10)

for _ in range(200):
    timmy.color(random_color())
    timmy.setheading(random.choice(angles))
    timmy.forward(30)

screen = Screen()
screen.exitonclick()
