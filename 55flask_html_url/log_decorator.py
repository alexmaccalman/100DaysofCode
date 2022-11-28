def logging_decorator(function):
    def wrapper(*args, **kwargs):
        print(f"You called the {function.__name__}{args}")
        result = function(args[0], args[1], args[2])
        print(f"The function returned: {result}")
    return wrapper

@logging_decorator
def a_function (a, b, c):
    return a * b * c

a_function(1,2,3)