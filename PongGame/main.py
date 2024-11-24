from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

game_on = True

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.tracer(0)

scoreboard = Scoreboard()

paddle_l = Paddle((-350, 0))
paddle_r = Paddle((350, 0))

ball = Ball()

screen.listen()
screen.onkeypress(paddle_r.go_up, "Up")
screen.onkeypress(paddle_r.go_down, "Down")
screen.onkeypress(paddle_l.go_up, "w")
screen.onkeypress(paddle_l.go_down, "s")

while game_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()

    if ball.distance(paddle_l) < 50 and ball.xcor() < -320 or ball.distance(paddle_r) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    if ball.xcor() > 355:
        ball.reset_pos()
        scoreboard.l_point()

    if ball.xcor() < -355:
        ball.reset_pos()
        scoreboard.r_point()

screen.exitonclick()