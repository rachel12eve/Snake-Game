from turtle import Turtle, position

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):  # determine what should initialise the snake
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for positions in STARTING_POSITIONS:
            self.add_segments(positions)

    def add_segments(self,positions):
        new_segment = Turtle("square")
        new_segment.color("White")
        new_segment.pu()
        new_segment.goto(positions)
        self.segments.append(new_segment)


    def extent(self):
        #add a new seg
        self.add_segments(self.segments[-1].position())



    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
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
