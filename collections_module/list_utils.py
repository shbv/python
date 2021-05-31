"""
deque:
    - double ended queue: generalization of stacks & queues
    - use for fast appends & pops (not random access, in that case use list)
"""
from collections import deque

# e.g. 1
l = ['a', 'b', 'c', 'd']
d = deque(l)
print(f"d: {d}")

# e.g. 2
d1 = deque()
print(f"d1: {d1}")
d1.append('a')
print(f"d1: {d1}")
d1.append('b')
print(f"d1: {d1}")
d1.appendleft('aa')
print(f"d1: {d1}")
d1.rotate(1)
print(f"d1: {d1}")
d1.rotate(-1)
print(f"d1: {d1}")

# e.g. 3
import string
print(f"last 10 alphabets: {string.ascii_lowercase[-10:]}")
d2 = deque(string.ascii_lowercase, 10) # maxlength of 10. Only last 10 will remain and rest popped out
print(f"d2: {d2}")

