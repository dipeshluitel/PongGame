from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 0)
        self.shape('circle')
        self.color('white')
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_bounch(self):
        self.y_move = self.y_move*-1
        self.move()

    def peddle_bounch(self):
        self.x_move = self.x_move*-1
        self.move()
