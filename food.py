from turtle import Turtle
import random

EDGE_MARGIN = 280

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("orange")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.penup()
        random_x = random.randint(-EDGE_MARGIN, EDGE_MARGIN)
        random_y = random.randint(-EDGE_MARGIN, EDGE_MARGIN)
        self.goto(random_x, random_y)
