"""A deque can be populated from either end, termed "left" and "right"."""

import collections

d1 = collections.deque()

# Add to the right
d1.extend('abcdefg')
print('extend : {}'.format(d1))
d1.append('h')
print('append : {}'.format(d1))


d2 = collections.deque()

# Add to the left
d2.extendleft(range(6))
print('extendleft : {}'.format(d2))
d2.appendleft(6)
print('appendleft : {}'.format(d2))


'''
Notes: The extendleft() function iterates over its input and performs the
equivalent of an appendleft() for each item.
'''

'''
OUTPUT:
extend : deque(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
append : deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
extendleft : deque([5, 4, 3, 2, 1, 0])
appendleft : deque([6, 5, 4, 3, 2, 1, 0])
'''