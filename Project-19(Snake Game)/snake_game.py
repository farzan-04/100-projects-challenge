from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snack Game")
screen.tracer(0) #setting it to 0 will turn this method off which is used for animation

#creating the snake
snake = Snake()
food = Food()
score = Scoreboard()

#controlling the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
#moving the snake
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collisions with the food
    if snake.head.distance(food) < 15:  #distance(food) will return the distance b/w the snake.head and food
        food.refresh()
        snake.extend_snake()
        score.your_score += 1
        score.refresh_score()

    #detect collisions with the wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        #game_is_on = False
        #score.game_over()
        score.reset()
        snake.reset()

    #detect collision with the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            # score.game_over()
            score.reset()
            snake.reset()

screen.exitonclick()
