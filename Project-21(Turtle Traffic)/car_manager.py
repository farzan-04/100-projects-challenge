import turtle
from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    cars = []
    car_speed = STARTING_MOVE_DISTANCE
    def __init__(self):
        super().__init__()
        self.hideturtle()
        # for color in COLORS:
        #     new_car = Turtle(shape= "square")
        #     new_car.penup()
        #     new_car.shapesize(stretch_wid= 1, stretch_len = 2)
        #     new_car.color(color)
        #     new_car.seth(180)
        #     y_pos = random.randint(-280, 280)
        #     new_car.goto(280, y_pos)
        #     self.cars.append(new_car)


    def generate_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.seth(180)
            y_pos = random.randint(-250, 250)
            new_car.goto(280, y_pos)
            self.cars.append(new_car)

    def move_cars(self):
      time.sleep(0.1)
      for car in self.cars:
          car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT









