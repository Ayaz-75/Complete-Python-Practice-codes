from turtle import Turtle, Screen


timmy = Turtle()

timmy.shape("turtle")
for tatu in range(4):
    timmy.forward(100)
    timmy.right(90)
# timmy.forward(100) this works the same as above block of code does
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)

screen = Screen()
screen.exitonclick()