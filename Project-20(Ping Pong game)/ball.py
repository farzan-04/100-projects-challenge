from turtle import Turtle


class Ball(Turtle):
    x_move = 10
    y_move = 10
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid= 1.25, stretch_len = 1.25)
        self.color("white")
        self.penup()
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def hit_wall(self):
        #self.y_increment = - self.y_increment
        self.y_move *= -1 #multiplying by -1 to convert sign
        self.move_speed *= 0.8

    def hit_paddle(self):
        self.x_move *= -1

    def restart(self):
        self.goto(0,0)
        self.x_move *= -1
