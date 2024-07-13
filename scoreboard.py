from turtle import Turtle


class Scoreboard(Turtle):
    """ I created this myself w/o looking at lesson. Go through the rest of the course and see how they do it."""
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.ht()
        self.goto(0, 260)
        self.color("white")
        self.speed("fastest")
        self.write(f"Score: {self.score}", align="center", font=('Arial', 18, 'normal'))

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=('Arial', 18, 'normal'))
