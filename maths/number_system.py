'''This python module demonstrates different types of number system.'''

class Conversion(object):
	'''This class performs conversion of one number system to the other.'''

	def __init__(self):
		self.hexa_ns = {
		    '0':0,
		    '1':1,
		    '2':2,
		    '3':3,
		    '4':4,
		    '5':5,
		    '6':6,
		    '7':7,
		    '8':8,
		    '9':9,
		    'A':10,
		    'B':11,
		    'C':12,
		    'D':13,
		    'E':14,
		    'F':15,
		}

	def anybase_to_decimal(self, i_value, base):
		'''Convert any base number system to decimal number system.'''
		decimal_num = 0
		for i in range(len(i_value)):
			decimal_num += int(self.hexa_ns[i_value[i]]) * base**(len(i_value)-i-1)
		print 'Given number %s of base \'%d\' in decimal number is: %d' % (
			i_value, base, decimal_num)

	def decimal_to_anybase(self, i_value, base):
		'''Convert decimal number to any base number system.'''
		temp = int(i_value)
		st = ''
		while base <= temp:
			# Retrieve appropriate dictionary key for a value.
			position_value = self.hexa_ns.keys()[self.hexa_ns.values().index(
				temp%base)]
			st = position_value + st
			temp /= base
		position_value = self.hexa_ns.keys()[self.hexa_ns.values().index(
				temp%base)]
		st = position_value + st
		print 'Given decimal number %s in base \'%d\' is: %s' % (
			i_value, base, st)


if __name__ == '__main__':
	print 'Number system: Conversion demonstration.'
	num_system_conversion = Conversion()
	num_system_conversion.anybase_to_decimal('101101', 2)
	num_system_conversion.anybase_to_decimal('565', 8)
	num_system_conversion.anybase_to_decimal('175', 16)
	num_system_conversion.anybase_to_decimal('ABC', 16)
	num_system_conversion.decimal_to_anybase('45', 2)
	num_system_conversion.decimal_to_anybase('373', 8)
	num_system_conversion.decimal_to_anybase('373', 16)
	num_system_conversion.decimal_to_anybase('2748', 16)