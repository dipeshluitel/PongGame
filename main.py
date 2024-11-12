from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
screen = Screen()

screen.setup(800, 600)
screen.title('PONG')
screen.bgcolor('black')
screen.tracer(0)

paddle_l = Paddle((350, 0))
paddle_r = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkeypress(paddle_l.move_up, "Up")
screen.onkeypress(paddle_l.move_down, "Down")

screen.onkeypress(paddle_r.move_up, "w")
screen.onkeypress(paddle_r.move_down, "s")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect wall bounch
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounch()

    # detect peddle bounch
    if (ball.xcor() > 340 and ball.distance(paddle_l) < 50) or (ball.xcor() < -340 and ball.distance(paddle_r) < 50):
        ball.peddle_bounch()
screen.exitonclick()
