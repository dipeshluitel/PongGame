from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(350, 0)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(350, new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(350, new_y)
