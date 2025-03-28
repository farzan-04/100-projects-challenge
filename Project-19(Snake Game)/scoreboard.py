from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        self.your_score = 0
        self.high_score = 0
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.write(f"score: {self.your_score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        self.speed("fastest")

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align = ALIGNMENT, font = FONT)

    def reset(self):
        if self.your_score > self.high_score:
            self.high_score = self.your_score
        self.your_score = 0
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(f"score: {self.your_score} High Score: {self.high_score}", align = ALIGNMENT, font = FONT)
