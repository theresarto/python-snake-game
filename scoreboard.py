from turtle import Turtle


ALIGN = "center"
FONT = ("Monospace", 18, "normal")


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
        with open("data.txt") as data:
            self.current_high_score = int(data.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"       Score: {self.score}   |   High Score: {self.current_high_score}", align=ALIGN, font=FONT)

    def update_score(self):
        self.score += 1
        if self.score >= self.current_high_score:
            self.current_high_score = self.score
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER.", align=ALIGN, font=("Monospace", 24, "normal"))

    def reset_highscore(self):
        self.write("Press [SPACE] to start.", align=ALIGN, font=("Monospace", 24, "normal"))
        if self.score >= self.current_high_score:
            self.current_high_score = self.score
            with open("data.txt", 'w') as data:
                data.write(f"{self.current_high_score}")
        self.score = 0
        self.update_scoreboard()

    def press_space_to_start(self):
        self.goto(0, 0)
        self.write("Press [SPACE] to start.", align=ALIGN, font=("Monospace", 24, "normal"))
