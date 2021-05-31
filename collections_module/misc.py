"""
Counter: returns map with counts
Works on most iterables (strings, tuples, lists, etc.). 
"""
print(" ==== Counter === ")
from collections import Counter
obj = 'tester'
counter = Counter(obj)
print(f"obj: {obj}, counts: {counter}, top2: {counter.most_common(2)}")
obj = ['aa', 'bb', 'cc', 'aa', 'aa', 'cc']
counter = Counter(obj)
print(f"obj: {obj}, counts: {counter}, top2: {counter.most_common(2)}")
print()
