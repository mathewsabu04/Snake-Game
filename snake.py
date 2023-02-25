from turtle import Turtle
#Starting position of the snake
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

#Made a clas called snake

class Snake:

    #Created the snake 
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    #Created the snake in the staring positions 
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    #added segements of the snake 
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    #To make the snake constanly moving 
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    #Makes the snake go up with the arrow keys
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    #Makes the snake go down with the arrow keys
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    #Makes the snake go left with the arrow keys
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
     
    #Makes the snake go right with the arrow keys
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
