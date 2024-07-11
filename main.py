from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Old School Snake Game")
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []


def generate_snake():
    x = 0
    y = 0
    for i in range(3):
        seg = Turtle()
        seg.shape("square")
        seg.color("white", "white")
        seg.penup()
        seg.goto(x, y)
        x -= 20
        segments.append(seg)


generate_snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for i in range(len(segments)-1, 0, -1):
        new_x = segments[i-1].xcor()
        new_y = segments[i-1].ycor()
        segments[i].goto(new_x, new_y)
    segments[0].left(90) # Change this to an event listener afterwards to the snake changes direction
    segments[0].forward(20) # Change the loop structure so that after event listener, the first segment keeps leading




screen.exitonclick()
