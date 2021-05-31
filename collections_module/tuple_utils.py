"""
namedtuple
"""
from collections import namedtuple

# regular tuple
t_reg = ('1234', 'abcd', 1.0)
print(f"regular tuple: {t_reg}, name element: {t_reg[1]}")

# named tuple
TupClass = namedtuple('TName', 'id name value')
t_named = TupClass(id='5678', name='efgh', value=2.0)
print(f"named tuple: {t_named}, name element: {t_named.name}")

# named tuple from a dict
d = {'id': '91011', 'name': 'ijkl', 'value': 3.0}
t_named_2 = namedtuple('TName2', 'id name value')(**d)
print(f"named tuple 2: {t_named_2}, name element: {t_named_2.name}")


