# Functions Inputs/Functionality/Output
def add(n1, n2):
    return n1 + n2


# Functions first class can be passed
def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)


# Nested functions
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    nested_function()


outer_function()


# Functions can be returned from other functions
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    return nested_function


inner_function = outer_function()
inner_function() # Triggers the nested function that returned



