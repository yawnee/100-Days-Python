from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Collision with Food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        #game_is_on = False
        score.reset()
        snake.reset()
        #score.game_over()

    # Detect collision with tail
    # If head collides with any snake segment in the tail, trigger game over
    for snakes in snake.snakes[1:]:
        if snake.head.distance(snakes) < 10:
            #game_is_on = False
            #score.game_over()
            score.reset()
            snake.reset()


screen.exitonclick()




