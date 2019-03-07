"""
ChainMap provides a convenience method for creating a new instance with one
extra mapping at the front of the maps list to make it easy to avoid modifying
the existing underlying data structures.
"""

import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m1 = collections.ChainMap(a, b)
m2 = m1.new_child()

print('m1 before:', m1)
print('m2 before:', m2)

m2['c'] = 'E'

print('m1 after:', m1)
print('m2 after:', m2)

# Note: This stacking behavoir is what makes it convenient to use ChainMap
# instances as template or application contexts. Specifically, it is easy to
# add or update values in one iteration, then discard the changes for the next
# iteration.

'''
OUTPUT:
$ python3 collections_chainmap_new_child.py 
m1 before: ChainMap({'c': 'C', 'a': 'A'}, {'c': 'D', 'b': 'B'})
m2 before: ChainMap({}, {'c': 'C', 'a': 'A'}, {'c': 'D', 'b': 'B'})
m1 after: ChainMap({'c': 'C', 'a': 'A'}, {'c': 'D', 'b': 'B'})
m2 after: ChainMap({'c': 'E'}, {'c': 'C', 'a': 'A'}, {'c': 'D', 'b': 'B'})
'''