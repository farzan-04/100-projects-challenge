from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 70, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.goto(320, 200)
        #self.write(f"Score: {self.r_score}", align=ALIGNMENT,font=FONT)  # when turtle reach the position then it writes so always put write() after goto()
        self.write(self.r_score, align=ALIGNMENT,font=FONT)  # when turtle reach the position then it writes so always put write() after goto()

        self.goto(-320, 200)
        #self.write(f"Score: {self.l_score}", align=ALIGNMENT,font=FONT)  # when turtle reach the position then it writes so always put write() after goto()
        self.write(self.l_score, align=ALIGNMENT,font=FONT)  # when turtle reach the position then it writes so always put write() after goto()

    def update_l_score(self):
        self.l_score += 1
        self.refresh_score()

    def update_r_score(self):
        self.r_score += 1
        self.refresh_score()
