# Turtle Race game:
import random
from turtle import Turtle , Screen, colormode
colormode(255)

color_list = ["red", "green", "blue", "yellow", "orange"]

screen = Screen()
screen.setup(width = 600, height = 400) #Set the size and position of the main window
user_bet = screen.textinput(title = "Make your bet", prompt = "which Turtle will win the race? Enter a color: ")  #Pop up a dialog window for input of a string.
print(user_bet)
# tim1 = Turtle(shape = "turtle")
# tim1.goto(-300, 0)
# tim2 = Turtle(shape = "turtle")
# tim2.goto(-300, -30)
# tim3 = Turtle(shape = "turtle")
# tim3.goto(-300,30)
# tim4 = Turtle(shape = "turtle")
# tim4.goto(-300,60)
# tim5 = Turtle(shape = "turtle")
# tim5.goto(-300,-60)

all_turtles = []
y_position = [0, 30, -30, 60, -60]
for turtle_index in range(0, 5):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.penup()
    new_turtle.color(color_list[turtle_index])
    new_turtle.goto(-280, y_position[turtle_index])
    all_turtles.append(new_turtle)

is_race_on = False
if user_bet in color_list:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 280:  # 280 is right border of screen as width(600)/2 - (size of turtle(40) / 2) = 280
            is_race_on = False
            winning_color = turtle.pencolor() #pencolor return only color of the turtle not the fill color but color does
            if user_bet == winning_color:
                print(f"You've won! The {winning_color} is the winner!")
            else:
                print(f"Sorry, You've lost! The {winning_color} is the winner!")
        else:
            turtle.speed("fastest")
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)


screen.exitonclick()

