"""Array data structure examples."""

import array
import binascii

def array_string():
    """Array is configured to hold a sequence of bytes and is initialized with
    a simple byte string.
    """
    s = b'This is the array.'
    a = array.array('b', s)
    print('As byte string:', s)
    print('As array      :', a)
    print('As hex        :', binascii.hexlify(a))

def array_sequence():
    """Array can be extended and otherwise manipulated in the same ways as
    other python sequences.
    """
    

if __name__ == '__main__':
    array_string()