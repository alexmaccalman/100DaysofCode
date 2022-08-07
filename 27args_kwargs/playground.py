def add(*args):
    print(args[0])
    sum = 0
    for n in args:
        sum += n
    return sum


print(add (1,5,5))

def calculate(n, **kwargs):
    # for key, value in kwargs:
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]

calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make") # use get to return nothing when nothing is passed to object
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seat")

my_car = Car(make="Nissan")
print(my_car.make)