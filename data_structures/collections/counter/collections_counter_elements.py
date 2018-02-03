"""
The elements() method returns an iterator that produces all of the items known
to the Counter.
"""

import collections

c = collections.Counter('extremely')
c['z'] = 0
print(c)
print(list(c.elements()))

# The order of elements is NOT guaranteed, and items with counts less than or
# equal to zero are not included.

'''
OUTPUT:
Counter({'e': 3, 'm': 1, 'l': 1, 'r': 1, 't': 1, 'y': 1, 'x': 1, 'z': 0})
['e', 'e', 'e', 'm', 'l', 'r', 't', 'y', 'x']
'''