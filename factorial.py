#!/usr/bin/python

# Method 1: Simple logic to find factorial of given number.
def factorial_of_num(num):
    fact = 1
    for i in range(1, num+1):
	if i <= num:
	  fact *= i
    return fact


# Method 2: Find factorial of given number using recursive technique.
def factorial_of_num_recursive(num):
    if num == 0:
      return 1
    return num * factorial_of_num_recursive(num-1)


if __name__ == '__main__':
    print "Enter a number to find its factorial:"
    num = int(input())
    print "The factorial of given number '%d' is '%d'" % (num,
	    factorial_of_num(num))
    print "The factorial of given number using recursive '%d' is '%d'" % (num,
	    factorial_of_num_recursive(num))
