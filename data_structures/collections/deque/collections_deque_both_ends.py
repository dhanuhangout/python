"""
Deques are thread-safe, the contents can even be consumed from both ends at the
same time from separate threads.
The threads in this example alternate between each end, removing items until
the deque is empty.
"""

import collections
import threading
import time


candle = collections.deque(range(5))


def burn(direction, nextSource):
	while True:
		try:
			next = nextSource()
		except IndexError:
			break
		else:
			print('{:>8}: {}'.format(direction, next))
			time.sleep(0.1)
	print('{:>8} done'.format(direction))
	return


if __name__ == '__main__':
	left = threading.Thread(target=burn,
		args=('Left', candle.popleft))
	right = threading.Thread(target=burn,
		args=('Right', candle.pop))
	left.start()
	right.start()

	left.join()
	right.join()


'''
OUTPUT:
 Left: 0
Right: 4
 Left: 1
Right: 3
 Left: 2
Right done
 Left done
'''