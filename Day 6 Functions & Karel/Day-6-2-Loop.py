#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

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

##### Don't need this for loop###
#for step in range(6):
#    function()
#################################

number_of_hurdles = 6
while number_of_hurdles > 0:
    function()
    number_of_hurdles -= 1
    print(number_of_hurdles)


#To keep the robot moving and stop at the goal do this:

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


# for step in range(6):
#    function()

number_of_hurdles = 3
while not at_goal():
    function()
