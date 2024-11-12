from turtle import Screen
from paddle import Paddle

screen = Screen()
paddle = Paddle()
screen.tracer(0)

screen.setup(800, 600)
screen.title('PONG')
screen.bgcolor('black')
screen.listen()
screen.onkeypress(paddle.move_up, "Up")
screen.onkeypress(paddle.move_down, "Down")

game_on = True
while game_on:
    screen.update()

screen.exitonclick()
