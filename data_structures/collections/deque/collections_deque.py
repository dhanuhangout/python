"""
A double-ended queue or deque, support adding and removing elements from
either end of the queue. The more commonly used stacks and queues are
degenerate forms of deques, where the inputs and outputs are restricted to a
single end.
"""

import collections

d = collections.deque('abcdefg')
print('Deque: {}'.format(d))
# Since deques are a type of sequence container, they support some of the same
# operations as list, such as examining the contents with __getitem__(),
# determining length, and removing elements from the middle of the queue by
# matching identity.
print('Length: {}'.format(len(d)))
print('Left end: {}'.format(d[0]))
print('Right end: {}'.format(d[-1]))

d.remove('c')
print('remove(c): {}'.format(d))


'''
OUTPUT:
Deque: deque(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
Length: 7
Left end: a
Right end: g
remove(c): deque(['a', 'b', 'd', 'e', 'f', 'g'])
'''