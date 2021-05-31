"""
defaultdict
OrderedDict
"""

"""
defaultdict
Initializes the object with a default_factory type (int, list, lambda functions, etc.) default value
"""
print(" ==== defaultdict === ")
from collections import defaultdict
dict1 = defaultdict(int)
dict1['x'] += 1
print(f"dict1['x']: {dict1['x']}, dict1['y']: {dict1['y']}")
dict2 = defaultdict(list)
dict2['x'].append("1")
print(f"dict2['x']: {dict2['x']}, dict2['y']: {dict2['y']}")
dict3 = defaultdict(lambda: "default_value")
dict3['x'] = 1
print(f"dict3['x']: {dict3['x']}, dict3['y']: {dict3['y']}")
print()

"""
OrderedDict
Keeps order of keys, also when we add new elements
"""
print(" ==== OrderedDict === ")
from collections import OrderedDict
d_t = {'c': 3, 'b': 2, 'a':1}
d_t = OrderedDict(sorted(d_t.items()))
print(f"d_t: {d_t}")
d_t['d'] = 4
d_t['e'] = 5
print(f"d_t: {d_t}")
print()

