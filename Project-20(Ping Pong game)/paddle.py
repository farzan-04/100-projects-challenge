from turtle import Turtle,Screen

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        #after inheriting Turtle class we don't need to create an object here to use its functions like self.paddle = Turtle(shape = "square")
        self.shape("square")
        self.shapesize(stretch_len= 1, stretch_wid= 5)
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y) #if we don't inherit Turtle then we have to write like this self.paddle.xcor()
                                                    # as xcor() work only with objects and paddle is but self not a object of Turtle

