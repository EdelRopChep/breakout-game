import turtle
import random

# Setup Game Screen
win = turtle.Screen()
win.title("Breakout Game")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

def move_left():
    x = paddle.xcor()
    if x > -250:
        paddle.setx(x - 20)

def move_right():
    x = paddle.xcor()
    if x < 250:
        paddle.setx(x + 20)

win.listen()
win.onkey(move_left, "Left")
win.onkey(move_right, "Right")

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, -230)
ball.dx = random.choice([-2, 2])
ball.dy = 2

# Bricks Setup
bricks = []
colors = ["red", "orange", "yellow", "green"]
for row in range(4):
    for col in range(7):
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(colors[row])
        brick.shapesize(stretch_wid=1, stretch_len=2)
        brick.penup()
        brick.goto(-210 + col * 70, 200 - row * 30)
        bricks.append(brick)

# Ball Movement & Collision Handling
def move_ball():
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Bounce off walls
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= -1

    # Bounce off the top
    if ball.ycor() > 290:
        ball.dy *= -1

    # Bounce off paddle
    if (ball.ycor() > -240 and ball.ycor() < -230) and (paddle.xcor()-50 < ball.xcor() < paddle.xcor()+50):
        ball.dy *= -1

    # Collision with bricks
    for brick in bricks:
        if ball.distance(brick) < 30:
            brick.goto(1000, 1000)  # Move it off-screen
            bricks.remove(brick)
            ball.dy *= -1

    # Lose condition
    if ball.ycor() < -290:
        ball.goto(0, -230)
        ball.dx = random.choice([-2, 2])
        ball.dy = 2

# Game Loop
while True:
    win.update()
    move_ball()