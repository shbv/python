"""
Decorators:
- Are callables that allow modifictions to other callables (functions, methods, classes, etc.)
- E.g.: decorate / wrap a function with another function (decorator)
    def my_decorator(func)
        ...
        return func

    def f():
        ...
    f = my_decorator(f)

        (or)
    
    @my_decorator
    def f():
        ...
"""

import functools

def decorator1(func):
    @functools.wraps(func)              # Copies metadata (__name__, __doc__, ..) from func to wrapper 
    def wrapper(*args, **kwargs):       # Collects the func args
        "decorator1 docstring"
        result = func(*args, **kwargs)  # Unpacks the args & pass to function
        result = result.upper() + " DEC1"
        return result
    return wrapper                      # This wrapper function is also called a closure in python, can access it outside decorator1 scope

def decorator2(func):
    @functools.wraps(func)
    def wrapper(arg1, arg2):
        "decorator2 docstring"
        result = func(arg1, arg2)
        result = result.swapcase() + " dec2"
        return result
    return wrapper

@decorator2
@decorator1
def myfunc(x, y):
    "myfunc docstring"
    return x + y

# function call
print(myfunc("test ", "decorator"))
print()
print("func name: ", myfunc.__name__)
print("func docstring: ", myfunc.__doc__)
