#Ping-Pong game

import time
from turtle import Turtle, Screen

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(height=600, width = 800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

#create paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
#create ball
ball = Ball()
#create scoreboard
scoreboard = Scoreboard()



screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #detect collision with top and bottom wall
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.hit_wall()
    #detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.hit_paddle()


    #Detect right paddle misses
    if ball.xcor() > 500 :
        ball.restart()
        scoreboard.update_l_score()
        ball.move_speed = 0.1
        

    #Detect left paddle misses
    if ball.xcor() < -500:
        ball.restart()
        scoreboard.update_r_score()
        ball.move_speed = 0.1



screen.exitonclick()
