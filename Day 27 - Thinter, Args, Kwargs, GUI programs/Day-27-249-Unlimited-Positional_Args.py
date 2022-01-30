# Notes:
# Keyword arguments
# def my_function(a, b, c):
# do this with a
# then this with b
# finally with c
# my_function(c=3, a=1, b=2)
# --------------------------
# Instead of this argument
# def add(n1, n2):
# return n1 + n2

# Use unlimited argument (it uses an *args). We can change the name like *numbers
# *args is a tuple
# def add(*args):
# for in args:
# print(n)
# add(3, 5, 7, 8)

def add(*args):
    for n in args:
        print(n)


add(3, 5, 7, 8)


def add(*args):
    print(args[0])  # prints first one of the function add(x,y,z...)
    print(args[1])
    sum = 0
    for x in args:
        sum += x
    return sum


print("")
print(add(3, 5, 7, 8))
