from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.x_speed = 20
        self.y_speed = 20
        self.move()
        self.move_speed = 0.1

    def move(self):
        if self.ycor() > 275 or self.ycor() < -270:
            self.y_speed *= -1

        new_x = self.xcor() + self.x_speed
        new_y = self.ycor() + self.y_speed

        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_speed *= -1
        self.move_speed *= 0.9

    def reset_pos(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        time.sleep(0.2)
        self.bounce_x()
