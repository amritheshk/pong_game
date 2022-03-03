from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.p1_score = 0
        self.p2_score = 0
        self.update()

    def update(self):
        self.clear()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(100, 200)
        self.write(arg=self.p1_score, align="center", font=("courier", 60, "normal"))
        self.goto(-100, 200)
        self.write(arg=self.p2_score, align="center", font=("courier", 60, "normal"))

    def increase_p1_score(self):
        self.p1_score += 1
        self.update()

    def increase_p2_score(self):
        self.p2_score += 1
        self.update()
