from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 18, "normal")


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
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER.", align=ALIGN, font= ("Arial", 24, "normal"))
