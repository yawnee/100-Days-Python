## Python Decorator Function
import time

def delay_decorator_function(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        # Do something after
    return wrapper_function

@delay_decorator_function
def say_hello():
    print('hello')

@delay_decorator_function
def say_bye():
    print('bye')

def say_greeting():
    print('greeting')

say_hello()
say_greeting()

decorated_function = delay_decorator_function(say_greeting) # Now "greeting" will be time sleep
decorated_function()
