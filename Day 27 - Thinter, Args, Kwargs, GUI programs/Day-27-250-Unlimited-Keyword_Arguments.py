def calculate(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
        print(kwargs["add"])


calculate(add=3, multiply=5)
print("")


def calculate1(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate1(2, add=3, multiply=5)
print("")


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs.get("model")  # "get" is used if value does not exist it will bring 'none'
        self.colour = kwargs.get("colour")
        self.seats = kwargs.get("seats")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
