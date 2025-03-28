from turtle import Turtle

STARTING_POSITION = [(0, 0,), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    #segments
    #STARTING_POSITION = [(0, 0,), (-20, 0), (-40, 0)]

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        # creating a snake

    def create_snake(self):
        for position in STARTING_POSITION:
           self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        # Snake.segments.append(segment) #we use class name if self is not used at the time of definition of attribute
        self.segments.append(segment)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

   
