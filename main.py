from turtle import Screen
import time

from scoreboard import Scoreboard

from food import Food
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("Black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()  # show after all three moved
    time.sleep(0.1)
    snake.move()

    # detect collission of food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extent()
        scoreboard.increase_score()

    # dectect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    # detect tail collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on == False
            scoreboard.game_over()

screen.exitonclick()
