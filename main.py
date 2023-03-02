from turtle import Screen
from paddle import *
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
score=Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # top and bottom colliding
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    # paddle colliding
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -340:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_positon()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_positon()
        score.r_point()







screen.exitonclick()