"""
It is possible to change the order of the keys in an OrderedDict by moving them
to either the beginning or the end of the sequence using move_to_end().
"""

import collections

d = collections.OrderedDict(
	[('a', 'A'), ('b', 'B'), ('c', 'C')]
)

print('Before:')
for k, v in d.items():
	print(k, v)

d.move_to_end('b')
print('move_to_end:')
for k, v in d.items():
	print(k, v)

d.move_to_end('b', last=False)
print('move_to_end(last=False):')
for k, v in d.items():
	print(k, v)

# The last argument tells move_to_end() whether to move the item to be last
# item in the key sequence (when True) or the first (when False).

'''
OUTPUT:
Before:
a A
b B
c C
move_to_end:
a A
c C
b B
move_to_end(last=False):
b B
a A
c C
'''