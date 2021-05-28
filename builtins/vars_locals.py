"""
- vars(x) returns x.__dict__ which usually exists for modules & class instances
- having vars() in function behaves same as having locals() in function: returns local variables in function as dict
Example from https://www.geeksforgeeks.org/vars-function-python/

"""

class Example(object):
    def __init__(self):
        self.v1 = "Example() __init__ var"

    def __repr__(self):
        return "Example() __repr__"

    def local(self):
        v3 = "Example() local() var"
        return locals()

    # Works same as locals()
    def vars_noargs(self):
        v4 = "Example() vars_noargs() var"
        return vars()

    def vars_withself(self):
        v5 = "Example() vars_withself():  not printed or returned"
        return vars(self)
	

if __name__ == "__main__":
    obj = Example()
    print(f"vars(obj): {vars(obj)}")
    # => vars(obj): {'v1': 'Example() __init__ var'}
    print(f"obj.local(): {obj.local()}")
    # => obj.local(): {'self': Example() __repr__, 'v3': 'Example() local() var'}
    print(f"obj.vars_noargs(): {obj.vars_noargs()}")
    # => obj.vars_noargs(): {'self': Example() __repr__, 'v4': 'Example() vars_noargs() var'}
    print(f"obj.vars_withselfj(): {obj.vars_withself()}")
    # => obj.vars_withselfj(): {'v1': 'Example() __init__ var'}

