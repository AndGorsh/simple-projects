import turtle
#spyrograph

turtle.speed(0)
turtle.bgcolor("black")
turtle.hideturtle()

a = 200

def draw_squares(a):
        turtle.forward(a)
        turtle.left(90)
        turtle.forward(a)
        turtle.left(90)
        turtle.forward(a)
        turtle.left(90)
        turtle.forward(a)
        turtle.left(90)

for i in range(18):
    for colours in ["red","magenta", "blue", "cyan", "green", "yellow", "white"]:
        turtle.color(colours)
        turtle.pensize(3)
        turtle.left(3)
        draw_squares(a)

turtle.mainloop()
