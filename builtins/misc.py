"""
any
all
eval
filter
map
zip
"""

l1 = [True, False, False]
l2 = [False, False, False]
l3 = [True, True, True]
l4 = ['xyz', '', '']

""" any """
print("== any: ==")
print(any(l1)) # True
print(any(l2)) # False
print(any(l3)) # True
print(any(l4)) # True

""" all """
print("== all: ==")
print(all(l1)) # False
print(all(l2)) # False
print(all(l3)) # True
print(all(l4)) # False

""" eval - not recommended"""
print("== eval: ==")
tmp = 5
x = 'tmp * 10'
print(f"{x} = {eval(x)}")

""" filter """
print("== filter: ==")
def filter_func(elem):
    return elem < 10
l = [5, 8, 50, 100]                 # iterable
print(filter(filter_func, l))       # iterator obj
print(list(filter(filter_func, l))) # list
print([elem for elem in l if filter_func(elem) is True]) # list

""" map """
print("== map: ==")
def map_func(elem):
    return elem * -1
l = [5, 8, 50, 100]                     # iterable
print(map(map_func, l))                 # iterator obj
print(list(map(map_func, l)))           # list
print([map_func(elem) for elem in l])   # list

""" zip """
l1 = ['k1', 'k2', 'k3']
l2 = ['v1', 'v2', 'v3']
print(zip(l1, l2))              # zip object
print(list(zip(l1, l2)))        # list of k,v
print(dict(zip(l1, l2)))        # dict of k,v

""" super """
class BaseClass():
    def __init__(self, a, b):
        print("baseclass __init__")
        self.a = a
        self.b = b
class SubClass1(BaseClass):
    def __init__(self, a, b):
        print("subclass1 __init__")
        super().__init__(a, b)  # In Python2: this was super(SubClass1, self).__init__(a, b) 
class SubClass2(BaseClass):
    def __init__(self, a, b):
        print("subclass2 __init__")
        super().__init__(a, b)   
class SubSubClass(SubClass1, SubClass2):
    pass
print("== subclass1 instantiate ==")
subclass1 = SubClass1(10, 20)
print(subclass1.a, subclass1.b)
print("== subsubclass instantiate ==")
subsubclass = SubSubClass(500, 1000)
print("== SubSubClass method resolution order ==")
print(SubSubClass.__mro__)

