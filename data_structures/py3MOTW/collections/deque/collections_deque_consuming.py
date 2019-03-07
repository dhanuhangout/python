"""The elements of the deque can be consumed from both ends of either end,
depending on the algorithm being applied.
"""

import collections

print('From the right: ')
d = collections.deque('abcdefg')

while True:
	try:
		print(d.pop(), end='')
	except IndexError:
		break
print()

print('From the left: ')
d = collections.deque(range(6))

while True:
	try:
		print(d.popleft(), end='')
	except IndexError:
		break
print()


'''
Notes: pop() is used to remove item from "right" end of the deque and popleft()
to take an item from the "left" end.
'''

'''
OUTPUT:
From the right: 
gfedcba
From the left: 
012345
'''