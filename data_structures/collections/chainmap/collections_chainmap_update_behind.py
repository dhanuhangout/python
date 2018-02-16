"""
A ChainMap does not cache the values in the child mappings. Thus, if their
contents are modified, the results are reflected when the ChainMap is accessed.
"""

import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)

print('Before: {}\n'.format(m['c']))

a['c'] = 'E'

print('After: {}\n'.format(m['c']))

# Note: Changing the values associated with existing keys and adding new
# elements works the same way.

'''
OUTPUT:
$ python3 collections_chainmap_update_behind.py 
Before: C

After: E
'''