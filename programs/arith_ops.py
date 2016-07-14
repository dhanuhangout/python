"""This module performs arithmetic operations."""

def add_two_nums(num1, num2):
    """Performs addition of two numbers."""
    return num1+num2

def mul_two_nums(num1, num2):
    """Performs multiplication of two numbers."""
    return num1*num2

def div_two_nums(num1, num2):
    """Performs division of two numbers."""
    return num1/num2

def mod_two_nums(num1, num2):
    """Performs modulo of two numbers."""
    return num1%num2

def sub_two_nums(num1, num2):
    """Performs subtraction of two numbers."""
    return num1-num2


DICT_OBJ = {
    1 : add_two_nums,
    2 : sub_two_nums,
    3 : mul_two_nums,
    4 : div_two_nums,
    5 : mod_two_nums
}


def main():
    """Starting of the program."""
    print "Selecet an arithmetic operation from below menu:"
    print "1. Addition\n2. Subtraction\n3. Multiplication\n4. Division"
    print "5. Modulo"
    option = int(raw_input())
    if option in DICT_OBJ.keys():
        print "Enter two numbers:"
        num1 = int(raw_input())
        num2 = int(raw_input())
        print DICT_OBJ[option](num1, num2)


if __name__ == '__main__':
    main()
