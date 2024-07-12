from turtle import Turtle


# STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# """ We don't actually need this because of our goto line """

MOVE_DISTANCE = 20


class Snake:
    """Creates the snake"""

    def __init__(self):
        self.segments = []
        self.generate()

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
        # Change this to an event listener afterwards to the snake changes direction
        # Change the loop structure so that after event listener,
        # the first segment keeps leading
        self.segments[0].forward(MOVE_DISTANCE)
