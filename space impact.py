import math
import turtle
import random
import os

# set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.tracer(1)
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
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -260)
player.setheading(90)
playerspeed = 15


# create the enemy
#enemy = turtle.Turtle()
#enemy.color("red")
#enemy.shape("circle")
#enemy.penup()
#enemy.speed(0)
#enemy.setposition(-200, 250)
#enemyspeed = 2

# CHOOSE A NUMBER OF ENEMIES
number_of_enemies = 5
# create an empty list of enemies
enemies = []

# add enemies to the list
for i in range(number_of_enemies):
    # create the enemy
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100,250)
    enemy.setposition(x, y)

enemyspeed = 2



# create player's bullet
bullet = turtle.Turtle()
bullet.color("white")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 40

# DEFINE BULLET STATE
# "READY" - ready to fire
# "FIRE" - bullet is firing
bulletstate = "ready"


# player movements
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    # declare bulletstate as a global if it needs changes
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        # move the bullet just above the player
        x = player.xcor()
        y = player.ycor() +10
        bullet.setposition(x, y)
        bullet.showturtle()


def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False


# create keyboard biding

turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

# MAIN GAME LOOP
while True:

    for enemy in enemies:
        # move enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        # move the enemy back and down
        if enemy.xcor() > 280:
            #MOVES ALL THE ENEMIES DOWN
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # CHANGE ENEMIES DIRECTION
            enemyspeed *= -1

        if enemy.xcor() < -280:
            # MOVES ALL THE ENEMIES DOWN
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #CHANGE ENEMIES DIRECTION
            enemyspeed *= -1

        #check for a collision between bullet and the enemy
        if isCollision(bullet, enemy):
            #reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            #reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)

        if isCollision(enemy, player):
            player.hideturtle()
            enemy.hideturtle()
            print("GAME OVER")
            break

    # MOVE THE BULLET
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    # check bullet reaching top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"












turtle.mainloop()
