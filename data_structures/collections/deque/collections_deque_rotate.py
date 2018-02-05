"""Deque has the ability to rotate it in either direction."""

import collections

d = collections.deque(range(10))
print('Normal : ', d)

d = collections.deque(range(10))
d.rotate(2)
print('Right rotation : ', d)

d = collections.deque(range(10))
d.rotate(-2)
print('Left rotation : ', d)


'''
Notes: Rotating the deque to the right (using a positive rotation) takes items
from the right end and moves them to the left end.
Rotating to the left (with a negative value) takes items from the left end and
moves them to the right end.
'''

'''
OUTPUT:
Normal :  deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
Right rotation :  deque([8, 9, 0, 1, 2, 3, 4, 5, 6, 7])
Left rotation :  deque([2, 3, 4, 5, 6, 7, 8, 9, 0, 1])
'''