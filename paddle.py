from turtle import Turtle

UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self,position):
        super(Paddle, self).__init__()
        self.create_paddle(position)

    def create_paddle(self,position):
        self.penup()
        self.goto(position)
        self.shape("square")
        self.setheading(90)
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.color("white")
        self.speed("fastest")

    def up(self):
        self.setheading(UP)
        self.forward(20)

    def down(self):
        self.setheading(DOWN)
        self.forward(20)
