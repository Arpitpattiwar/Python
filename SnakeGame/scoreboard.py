from turtle import Turtle

FONT = ("Arial", 20, "normal")
ALIGN = "center"


class Scoreboard(Turtle):

    def __init__ (self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.pu()
        self.goto(0, 270)
        self.hideturtle()
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def increase(self):
        self.clear()
        self.score +=1
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!!", align=ALIGN, font=FONT)