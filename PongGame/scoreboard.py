from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 60, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.goto(-80, 210)
        self.write(self.l_score, align=ALIGN, font=FONT)
        self.goto(80, 210)
        self.write(self.r_score, align=ALIGN, font=FONT)

    def l_point(self):
        self.clear()
        self.l_score += 1
        self.update()

    def r_point(self):
        self.clear()
        self.r_score += 1
        self.update()
