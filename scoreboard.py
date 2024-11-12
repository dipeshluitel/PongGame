from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=("courier", 80, "normal"))
        self.goto((100, 200))
        self.write(self.r_score, align='center', font=("courier", 80, "normal"))

    def increment_r(self):
        self.r_score = 1
        self.update_score()

    def increment_l(self):
        self.l_score = 1
        self.update_score()