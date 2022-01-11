from turtle import Turtle

STARTING_POSITION = starting_positions = [(0, 0), (-20, 0), (-40, 0)]  # constant
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for position in starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        # add a new segment to the snake
        new_snake = Turtle(shape="square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.snakes.append(new_snake)

    def extend(self):
        # Add a new segment to the snake.
        self.add_segment(self.snakes[-1].position())

    def move(self):
        for seg_number in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[seg_number - 1].xcor()
            new_y = self.snakes[seg_number - 1].ycor()
            self.snakes[seg_number].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

