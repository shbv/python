"""
Python allows objects to be callable functions using __call__ method
callable(obj) returns True for objects which are callable
"""

class Temp1:
    def __init__(self, msg):
        self.msg = msg
        print("Temp1 __init__")

    def __call__(self):
        print(self.msg + " is now called")

class Temp2:
    def __init__(self, msg):
        self.msg = msg
        print("Temp2 __init__")


t1 = Temp1('temp1')
print("t1 is callable: ", callable(t1))
t1()
print()

t2 = Temp2('temp2')
print("t2 is callable: ", callable(t2))
t2()


