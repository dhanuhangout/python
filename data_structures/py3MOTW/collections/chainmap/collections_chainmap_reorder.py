"""
The ChainMap stores the list of mappings over which it searches in a list in
its maps attribute. This list is mutable, so it is possible to add new mappings
directly or to change the order of the elements to control lookup and update
bhevior.
"""

import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)

print(m.maps)
print('c = {}\n'.format(m['c']))

# reverse the list
m.maps = list(reversed(m.maps))

print(m.maps)
print('c = {}\n'.format(m['c']))

# Note: When the list of mappings is reversed, the value associated with 'c'
# changes.

'''
OUTPUT:
$ python3 collections_chainmap_reorder.py 
[{'c': 'C', 'a': 'A'}, {'b': 'B', 'c': 'D'}]
c = C

[{'b': 'B', 'c': 'D'}, {'c': 'C', 'a': 'A'}]
c = D
'''