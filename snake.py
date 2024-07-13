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

    def generate(self):
        """Starting position in this code"""
        x = 0
        y = 0
        for i in range(3):
            seg = Turtle()
            seg.shape("square")
            seg.color("white", "white")
            seg.penup()
            seg.goto(x, y)
            x -= 20
            self.segments.append(seg)

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
        if self.head.xcor() == -EDGE \
                or self.head.xcor() == EDGE \
                or self.head.ycor() == -EDGE \
                or self.head.ycor() == EDGE:
            return True

    def hit_tail(self):
        """ I created this myself w/o looking at lesson. Go through the rest of the course and see how they do it."""
        for i in range(1, len(self.segments) - 1):
            if self.head.distance(self.segments[i]) < 5:
                return True

    def generate_tail(self):
        """ I created this myself w/o looking at lesson. Go through the rest of the course and see how they do it."""
        seg = Turtle()
        seg.shape("square")
        seg.color("white", "white")
        seg.penup()
        new_x = self.segments[-1].xcor()
        new_y = self.segments[-1].ycor()
        seg.goto(new_x, new_y)
        self.segments.append(seg)
        self.segments[-1].goto(new_x, new_y)
