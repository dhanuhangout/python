"""collections defaultdict example."""

import collections

def default_factory():
	return 'default value'


if __name__ == '__main__':
	d = collections.defaultdict(default_factory, foo='bar')
	print('d: {}'.format(d))
	print('foo => {}'.format(d['foo']))
	print('bar => {}'.format(d['bar']))


'''
OUTPUT:
d: defaultdict(<function default_factory at 0x7fbdd8c696e0>, {'foo': 'bar'})
foo => bar
bar => default value
'''