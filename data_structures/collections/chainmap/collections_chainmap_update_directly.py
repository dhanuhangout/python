"""
It is possible to set values through the ChainMap directly, although only the
first mapping in the chain is actually modified.
"""

import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)

print('Before:', m)

m['c'] = 'E'

print('After:', m)
print('a:', a)

# Note: When the new value is stored using m, the a mapping is updated.

'''
OUTPUT:
$ python3 collections_chainmap_update_directly.py 
Before: ChainMap({'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'})
After: ChainMap({'a': 'A', 'c': 'E'}, {'b': 'B', 'c': 'D'})
a: {'a': 'A', 'c': 'E'}
'''