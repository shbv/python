"""
python -m timeit -n 1000 -r 3 -s "import timeit_mod" "timeit_mod.func()"
    -> repeat 3 times, setup "import timeit_mod", code statement "timeit_mod.func()"
python timeit_mod.py
"""

def func():
    x = 5*10

if __name__ == "__main__":

    import timeit

    # simple code
    print(timeit.timeit(stmt="a=10; b=20; s=a+b", number=1000)) #prints time for 1000 iterations of stmt

    # function
    setup = "from __main__ import func" # setup executed only once
    print(timeit.timeit(stmt="func()", setup=setup, number=1000)) #prints time for 1000 iterations of stmt

    # timeit.repeat
    setup = "from __main__ import func"
    print(timeit.repeat(stmt="func()", setup=setup, repeat=5, number=1000)) #prints time for 1000 iterations of stmt 5 times




