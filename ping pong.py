import turtle
# SCREEN SETUP
wn = turtle.Screen()
wn.title("Ping Pong by AndGorsh")
wn.bgcolor("#2F4F4F")
wn.setup(width=800, height=600)
wn.tracer(0)

# SCORES
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("#FF6347")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("#F4A460")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# BALL
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("#9932CC")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# PEN
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.color("#FFF8DC")
pen.penup()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))


# FUNCTIONS
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keybord binding
wn.listen()

wn.onkey(paddle_a_up, "e")
wn.onkey(paddle_a_down, "s")
wn.onkey(paddle_b_up, "Up")
wn.onkey(paddle_b_down, "Down")

#MAIN LOOP
while True:
    wn.update()

# Ball moves
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

# Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

# PADDLE AND BALL COLLISIONS
    if (ball.xcor() > 320 and ball.xcor() > 330) and (ball.ycor() < paddle_b.ycor() +40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(320)
        ball.dx *= -1

    if (ball.xcor() < -320 and ball.xcor() < -330) and (ball.ycor() < paddle_a.ycor() +40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-320)
        ball.dx *= -1

