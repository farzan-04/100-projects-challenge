from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        self.your_score = 0
        #Read high score from data.txt
        with open("data.txt") as data:
            self.high_score = int(data.read())
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
            #Store high score into data.txt
            with open("data.txt", mode = "w") as data:
                data.write(str(self.high_score))
        self.your_score = 0
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(f"score: {self.your_score} High Score: {self.high_score}", align = ALIGNMENT, font = FONT)
