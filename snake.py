from turtle import Screen, Turtle
import time

# Constants
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():
    # What will happen when we initialize a new snake object
    def __init__(self):
        self.segments = []
        self.x_axis = 0
        self.y_axis = 0
        self.create_snake()
        self.head = self.segments[0]


    # Create Snake
    def create_snake(self):
        for position in range(3):
            self.add_segment(position)


    def add_segment(self, position):
        new_segment = Turtle(shape="turtle")
        new_segment.color("white")
        new_segment.penup()
        #new_segment.shapesize(2)
        new_segment.goto(x=self.x_axis, y=self.y_axis)
        self.x_axis -= 20
        self.segments.append(new_segment)


    # Adds new segment to the snake
    def extend(self):
        # Everything in the brackets determines the position of the added segment
        self.add_segment(self.segments[-1].position()) # example [1,2,3]; here the -1 position would be 3


    # Gets snake to automatically move forwards
    def move(self):
            # Move the segments in reverse order
            for seg_num in range(len(self.segments) - 1, 0, -1):  # range(start=2, stop=0, step=-1)
                # Get the x coordinates of the segment in front.
                new_x = self.segments[seg_num - 1].xcor()
                # Get the y coordinates of the segment in front.
                new_y = self.segments[seg_num - 1].ycor()
                # Move the current segment to the position of the segment in front of it.
                self.segments[seg_num].goto(new_x, new_y)
            self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)