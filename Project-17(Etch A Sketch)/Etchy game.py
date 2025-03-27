#Etchy game

from turtle import Turtle , Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_left():
    current_direction = tim.heading() + 10 #this is how left is derived
    tim.seth(current_direction)
    #tim.left(10)

def move_right():
    current_direction = tim.heading() - 10 # this is how right is derived
    tim.seth(current_direction)
    #tim.right(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.down()


screen.listen()
screen.onkey(key= "w", fun= move_forward) #this function does not return any value and can accept positional as well as keyword argument
screen.onkey(move_backward, "s")
screen.onkey(fun= move_left, key = "l")
screen.onkey(key= "r", fun=move_right)
screen.onkey(key= "r", fun=move_right)
screen.onkey(key= "c", fun=clear)

screen.exitonclick()
