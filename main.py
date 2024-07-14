from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Old School Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Updates the screen and scoreboard when the snake eats the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.generate_tail()
        scoreboard.update_score()
    # Detect collision with the edge of the screen or the tail
    if snake.edge_of_screen() or snake.hit_tail():
        # scoreboard.press_space_to_start()
        scoreboard.reset_highscore()
        screen.onkey(fun=snake.reset, key="space")
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.generate_tail()
            scoreboard.update_score()

        # scoreboard.game_over()

screen.exitonclick()
