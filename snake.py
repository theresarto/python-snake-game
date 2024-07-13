from turtle import Turtle

# STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# """ We don't actually need this because of our goto line """

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


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
        if self.head.xcor() == -300 \
                or self.head.xcor() == 300 \
                or self.head.ycor() == -300 \
                or self.head.ycor() == 300:
            return True
