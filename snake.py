from turtle import Turtle

# STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# """ We don't actually need this because of our goto line """

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

EDGE = 300


class Snake:
    """Creates the snake"""

    def __init__(self):
        self.segments = []
        self.generate()
        self.head = self.segments[0]

    def create_segment(self):
        """ This can actually be outside the class, but for purposes of contextualisation, I'm keeping this in """
        segment = Turtle()
        segment.shape("square")
        segment.color("white", "white")
        segment.penup()
        return segment

    def generate(self):
        """Starting position in this code"""
        x = 0
        y = 0
        for i in range(3):  # Chose range so that you can easily adjust the length of snake
            segment = self.create_segment()
            segment.goto(x, y)
            x -= 20  # x-variable allows you to keep making starting segments, without a fixed list [(0,0), (-20,0)...]
            self.segments.append(segment)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)

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

    def edge_of_screen(self):
        return abs(self.head.xcor()) == EDGE or abs(self.head.ycor()) == EDGE

    def hit_tail(self):
        """ I created this myself w/o looking at lesson. Go through the rest of the course and see how they do it."""
        for segment in self.segments[1:]: # Excludes 0 because that's the snake head
            if self.head.distance(segment) < 5:
                return True

    def generate_tail(self):
        """Generate a new segment and append it to the end of the snake."""
        new_x = self.segments[-1].xcor()
        new_y = self.segments[-1].ycor()
        new_segment = self.create_segment()
        new_segment.goto(new_x, new_y)
        self.segments.append(new_segment)
