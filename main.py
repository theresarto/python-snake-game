from turtle import Screen, Turtle
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Old School Snake Game")
screen.tracer(0)

# def generate_snake():
#     x = 0
#     y = 0
#     for i in range(3):
#         seg = Turtle()
#         seg.shape("square")
#         seg.color("white", "white")
#         seg.penup()
#         seg.goto(x, y)
#         x -= 20
#         segments.append(seg)
#
#
# generate_snake()
snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
