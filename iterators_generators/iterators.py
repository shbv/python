"""
__iter__: returns iterator object
__next__: returns next element in iteration

iterable: object with __iter__ method
iterator: object with __iter__ & __next__ methods. Allows to iterate over a container

How to call:
    - Use for loop or list comprehension on object
    - Use Python built-ins iter & next (for iterators)

Examples:
    - list is iterable, but not iterator.  (Can check using next(list_object))
"""

""" Python list """
l = [1, 2, 3]
# next(l) raises TypeError, since its not iterator
l_iter = iter(l)    # turns it into iterator
next(l_iter)
next(l_iter)
next(l_iter)        
#next(l_iter)        # raises StopIteration. Does not happen with for loop

""" Custom iterator """
class CustomIterator:

    def __init__(self, elements):
        self.elements = elements
        self.ix = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.ix >= len(self.elements): 
            raise StopIteration
        next_element = self.elements[self.ix]
        self.ix += 1
        return next_element

custom_obj = CustomIterator([1, 2, 3])
for element in custom_obj:
    print(element)

