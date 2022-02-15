import turtle as t
import random
from turtle import Turtle, Screen

t.colormode(255)
timmy = Turtle()
screen = Screen()
timmy.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    ran_c = (r, g, b)
    return ran_c


def draw_spiro(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spiro(5)
screen.exitonclick()
