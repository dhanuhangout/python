import number_system
import unittest

class TestNumberSystemConversion(unittest.TestCase):
    def setUp(self):
    	self.conversion = number_system.Conversion()

    def test_anybase_to_decimal(self):
        ret_value = self.conversion.anybase_to_decimal('101101', 2)
        print 'ret_value = ', ret_value
        assert(ret_value == 45)


if __name__ == '__main__':
    unittest.main()
