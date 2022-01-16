import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# The player will spawn at the position
player = Player((0, -250))
level = Scoreboard()
cars = CarManager()

# Player 1 Controls
screen.listen()
screen.onkeypress(player.up, "w")

# The speed of the cars
new_speed = 5

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.car_spawn()
    cars.car_move(new_speed)

    # When frogger reaches the end: increase level
    if player.ycor() > 250:
        level.increase_score()
        new_speed = new_speed + 5
        print(f'Speed increased: {new_speed}')
        player.respawn((0, -250))

    # Frogger death by car
    for each_car in cars.all_cars:
        if each_car.distance(player) < 27:
            level.game_over()
            game_is_on = False




screen.exitonclick()
