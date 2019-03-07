"""
For situations where the new context is known or built in advance, it is also
possible to pass a mapping to new_child().
"""

import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}
c = {'c': 'E'}

m1 = collections.ChainMap(a, b)
m2 = m1.new_child(c)
m3 = collections.ChainMap(c, *m1.maps)

print('m1["c"] = {}'.format(m1['c']))
print('m2["c"] = {}'.format(m2['c']))
print('m3["c"] = {}'.format(m3['c']))

'''
OUTPUT:
$ python3 collections_chainmap_new_child_explicit.py 
m1["c"] = C
m2["c"] = E
m3["c"] = E
'''