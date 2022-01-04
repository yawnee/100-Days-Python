#from turtle import Turtle as t, Screen as s  # can alias the names
#import random


# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color('red')

# TODO: DRAW A SQUARE
# tim = t()
# tim.shape("triangle")
# tim.forward(100)
# for number in range(3):
#     tim.left(90)
#     tim.forward(100)

# TODO: Draw a dashed Line
# tim = t()
# tim.shape("triangle")
# for x in range (20):
#     tim.pd()
#     tim.forward(10)
#     tim.pu()
#     tim.forward(10)

# TODO: Drawing Different Shapes with random colours: Triangle, square, pentagon, hexagon, heptagon, octagon,
#  nonagon, decagon
# tim = t()
# tim.shape("triangle")
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 10):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)

# TODO: Challenge: Generate a random walk
# tim = t()
# tim.shape("triangle")
# tim.pensize(10)
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# direction = ['left', 'right', 'straight']
#
# for random_walk in range(random.randint(50, 200)):
#     tim.color(random.choice(colours))
#     choice = random.choice(direction)
#     if choice == 'left':
#         tim.left(90)
#         tim.forward(50)
#     elif choice == 'right':
#         tim.right(90)
#         tim.forward(50)
#     elif choice == 'forward':
#         tim.forward(50)
#
# # Instructor code:
# tim = t()
# tim.shape("triangle")
# tim.pensize(15)
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# directions = [0, 90, 180, 270]
#
# for _ in range(200):
#     tim.color(random.choice(colours))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# TODO: Generate random RGB colours
# Tuple is a datatype with (1,2,3), similar to a list but are ordered
# Tuple are carved in stone and cannot be changed
# my_tuple = (1, 3, 8)
# print(my_tuple[1])
#
# import turtle as t
# import random
# tim = t()
# tim.shape("triangle")
# tim.pensize(15)
# direction = [0, 90, 180, 270]
# t.colormode(255)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     rgb = (r, g, b)
#     return rgb
#
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(direction))

# TODO: Draw a spirograph
# import turtle as t
# import random
#
# tim = t.Turtle()
# t.colormode(255)
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     rgb = (r, g, b)
#     return rgb
#
#
# tim.speed("fastest")
#
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
#
#
# draw_spirograph(5)







screen = t.Screen()
screen.exitonclick()
