import time
import turtle
from turtle import Screen
from venv import create

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#create player
player = Player()
#create cars
car_manager = CarManager()
#create scoreboard
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
#start_time = time.time() #give the current time
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # if time.time() - start_time >= 0.5:
    #     car_manager.generate_cars()
    #     start_time = time.time() #reset timer
    #
    car_manager.generate_cars()
    car_manager.move_cars()
    #detect collision with car
    for car in car_manager.cars:
        if car.distance(player) < 22:
            game_is_on = False
            scoreboard.game_over()
    #detect a successful crossing
    if player.is_at_finish_line():
        player.goto_start()
        car_manager.level_up()
        scoreboard.level += 1
        scoreboard.update_level()

#turtle.ontimer(car_manager.generate_cars, 1000)

screen.exitonclick()
