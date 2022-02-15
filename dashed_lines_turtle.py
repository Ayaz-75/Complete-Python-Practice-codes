from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("arrow")

colours = ["Green", "red", "blue", "indigo", "violet", "orange", "yellow", "cyan"]


def draw_shape(number_of_sides):
    for _ in range(number_of_sides):
        angle = 360 / number_of_sides
        timmy.forward(100)
        timmy.right(angle)


for _ in range(3, 11):
    timmy.color(random.choice(colours))
    draw_shape(_)

screen = Screen()
screen.exitonclick()

#
# for _ in range(10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()
#     timmy.forward(10)
#
# for _ in range(10):
#     timmy.right(135)
#     timmy.forward(100)
#     timmy.right(90)
#     timmy.forward(100)
#     timmy.dot()
#     timmy.color("green")
#     timmy.fillcolor("red")
#
# for _ in range(3):
#     timmy.forward(100)
#     timmy.right(120)
# for _ in range(4):
#     timmy.color("red")
#     timmy.forward(100)
#     timmy.right(90)
# for _ in range(5):
#     timmy.color("green")
#     timmy.forward(100)
#     timmy.right(72)
#
# for _ in range(6):
#     timmy.color("yellow")
#     timmy.forward(100)
#     timmy.right(60)
# for _ in range(7):
#     timmy.color("blue")
#     timmy.forward(100)
#     timmy.right(51.4285)
#
# for _ in range(8):
#     timmy.color("red")
#     timmy.forward(100)
#     timmy.right(45)
#
# for _ in range(9):
#     timmy.color("violet")
#     timmy.forward(100)
#     timmy.right(40)
#
# for _ in range(10):
#     timmy.color("orange")
#     timmy.forward(100)
#     timmy.right(36)
