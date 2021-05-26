"""
Scopes: local, global, nonlocal
"""

"""
local scope
"""
def local_func(a):
    
    #print(f"local_func before: x={x}")
    #  => Gives UnboundLocalError since x is assigned later. If x is not assigned later, picks x from global scope
    print(f"local_func before: a={a}")

    x = 200
    a = 201
    
    print(f"local_func after: x={x}")
    print(f"local_func after: a={a}")


"""
global scope
"""
def global_func(a):
    
    # implies x is available for this code block
    global x 

    print(f"global_func before: x={x}")
    print(f"global_func before: a={a}")

    x = 300  # not recommended to change globals inside functions
    a = 301
    
    print(f"global_func after: x={x}")
    print(f"global_func after: a={a}")
    

"""
nonlocal scope:
reference/assign to variables in outer scope of function, but not at global scope
"""
def nonlocal_func():

    x = 0 # runs only when nonlocal_func is assigned to an object. Calling object() will not run this again.

    def incr():
        nonlocal x  # => Gives UnboundLocalError without it since x is assigned later.
        x += 1
        return x

    return incr


if __name__ == '__main__':

    x = 100

    print(f"main before local_func: x={x}")
    local_func(x)
    print(f"main after local_func: x={x}")

    print(f"main before global_func: x={x}")
    global_func(x)
    print(f"main after global_func: x={x}")

    print(f"main nonlocal_func:")
    nonlocal_func_t = nonlocal_func()
    print(f"x={nonlocal_func_t()}")
    print(f"x={nonlocal_func_t()}")
    print(f"x={nonlocal_func_t()}")

