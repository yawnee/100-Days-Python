#python.org/3/library/functions

#def my_function():
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def function():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


for step in range(6):
    function()