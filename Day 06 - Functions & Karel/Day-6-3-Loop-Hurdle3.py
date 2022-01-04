def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    while not front_is_clear():
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()