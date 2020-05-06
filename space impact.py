import turtle
import os

# set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

# draw border

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pensize(3)
border_pen.pendown()

for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)

border_pen.hideturtle()

# create a player turtle





turtle.mainloop()
