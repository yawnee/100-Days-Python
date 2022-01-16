import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
CARS = []
STARTING_MOVE_DISTANCE = 15
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def car_move(self, new_speed):
        # This takes the cars in 'all_cars' into movement
        for each_car in self.all_cars:
            each_car.backward(new_speed)

    def car_spawn(self):
        # This is to keep the list short
        # if len(self.all_cars) > 20:
        #     self.all_cars.pop(0)
        # This is to reduce amount of car respawn spam
        random_chance = random.randint(1, 6)
        if random_chance == 6:
            new_car = Turtle('square')
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y_spawn = random.randint(-230, 230)
            random_x_spawn = random.randint(300, 320)
            new_car.goto(random_x_spawn, random_y_spawn)
            self.all_cars.append(new_car)
