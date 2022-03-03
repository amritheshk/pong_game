from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard_pong import Scoreboard
import time

SLEEP_TIME = 0.03
# TODO make a screen
screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("THE PONG")
screen.tracer(0)

# TODO import paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
# TODO import ball
ball = Ball()
# TODO import scoreboard
scoreboard = Scoreboard()
# TODO make a center boundary line
drawer = Turtle()
drawer.hideturtle()
drawer.goto(0, 300)
drawer.setheading(270)
drawer.color("white")
drawer.forward(600)

end = False
while not end:
    time.sleep(ball.move_speed)
    screen.update()
    # TODO control paddle movement
    screen.listen()
    screen.onkeypress(fun=l_paddle.up, key="w")
    screen.onkeypress(fun=l_paddle.down, key="s")
    screen.onkeypress(fun=r_paddle.up, key="Up")
    screen.onkeypress(fun=r_paddle.down, key="Down")
    # TODO ball movement and bounce logic
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # TODO detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 325 or ball.distance(l_paddle) < 50 and ball.xcor() < -325:
        ball.bounce_x()
    # TODO detect when paddle misses
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.increase_p2_score()
    elif ball.xcor() < -400:
        ball.reset_position()
        scoreboard.increase_p1_score()
screen.exitonclick()
