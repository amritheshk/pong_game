from turtle import Turtle
import time

BOTTOM_WALL_Y=-280
UPPER_WALL_Y=280

class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.shape("circle")
        self.move_speed=0.1
        self.penup()
        self.color("white")
        self.x_move=10
        self.y_move=10
    def move(self):
        new_xcor=self.xcor()+self.x_move
        new_ycor=self.ycor()+self.y_move
        self.goto(new_xcor,new_ycor)
    def bounce_y(self):
        self.y_move *= -1
    def bounce_x(self):
        self.x_move*=-1
        self.move_speed *= 0.7
    def reset_position(self):
        self.home()
        self.x_move*=-1
        self.y_move*=-1
        self.move_speed=0.1