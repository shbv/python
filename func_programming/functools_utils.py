"""
functools.*
    partial
    typing / type hinting
    singledispatch
"""

""" 
partial: 
    create function with frozen/default args
"""

from functools import partial
def func(x, y, z):
    return x + y + z
func_t = partial(func, 1, 2)
print("=== partial func ===")
print(func_t(3))
print()

""" 
typing / type hinting:
    declare args/return to have certain type, but its not binding & can be violated
"""    
print("=== typing / type hinting: ===")
def func_new(x: int, y: str, z: list) -> bool:
    return (x in z or y in z)
print(func_new(1, 'yes', [0, 'no']))
print(func_new(0, 'yes', [0, 'no']))
print(func_new(1.1, 'no', [0, 'no']))
print(func_new(0, 1.1, [0, 'no']))
print()

""" 
singledispatch: 
    Useful for function overloading with different types, based on first argument to function 
"""
from functools import singledispatch
print("=== singledispatch ===")

@singledispatch
def add_func(a, b):
    raise NotImplementedError('Unsupported first argument type')

@add_func.register(str)
@add_func.register(int)
@add_func.register(float)
def _(a, b):
    # accepts int or str for a
    print(f"first argument type is {type(a)}")
    res = a + b
    print(f"a: {a}, b: {b}, result: {res}")

@add_func.register(list)
def _(a: list, b: list) -> list:
    # accepts list
    print(f"first argument type is {type(a)}")
    res = a + b + ['end']
    print(f"a: {a}, b: {b}, result: {res}")

add_func(1.1, 2.2)
add_func(1, 2)
add_func('abc', 'xyz')
add_func(['m', 'n', 'o'], ['d', 'e', 'f'])
add_func({}, 2) # returns NotImplementedError


