"""
Any empty Counter can be constructed with no arguments and populated via
update() method.
"""

import collections

c = collections.Counter()
print('Initial :', c)

c.update('abcdaab')
print('Sequence:', c)

c.update({'a': 1, 'd': 5})
print('Dict: ', c)

'''
OUTPUT:
('Initial :', Counter())
('Sequence:', Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1}))
('Dict: ', Counter({'d': 6, 'a': 4, 'b': 2, 'c': 1}))
'''