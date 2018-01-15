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
        for i in i_value:
            decimal_num += int(self.hexa_ns[i_value[i]]) * base**(len(i_value)-i-1)
        print 'Given number %s of base \'%d\' in decimal number is: %d' % (
            i_value, base, decimal_num)

    def decimal_to_anybase(self, i_value, base):
        '''Convert decimal number to any base number system.'''
        temp = int(i_value)
        converted_num = ''
        while base <= temp:
            # Retrieve appropriate dictionary key for a value.
            position_value = self.hexa_ns.keys()[self.hexa_ns.values().index(
                temp%base)]
            converted_num = position_value + converted_num
            temp /= base
        position_value = self.hexa_ns.keys()[self.hexa_ns.values().index(
            temp%base)]
        converted_num = position_value + converted_num
        print 'Given decimal number %s in base \'%d\' is: %s' % (
            i_value, base, converted_num)


if __name__ == '__main__':
    print 'Number system: Conversion demonstration.'
    NUM_SYSTEM_CONVERSION = Conversion()
    NUM_SYSTEM_CONVERSION.anybase_to_decimal('101101', 2)
    NUM_SYSTEM_CONVERSION.anybase_to_decimal('565', 8)
    NUM_SYSTEM_CONVERSION.anybase_to_decimal('175', 16)
    NUM_SYSTEM_CONVERSION.anybase_to_decimal('ABC', 16)
    NUM_SYSTEM_CONVERSION.decimal_to_anybase('45', 2)
    NUM_SYSTEM_CONVERSION.decimal_to_anybase('373', 8)
    NUM_SYSTEM_CONVERSION.decimal_to_anybase('373', 16)
    NUM_SYSTEM_CONVERSION.decimal_to_anybase('2748', 16)
