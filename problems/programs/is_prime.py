#!/usr/bin/python

def is_prime_num(num):
    if num > 1:
      for i in range(2, num):
	  if num%i == 0:
	    print "The given number is divisible by '%d' and hence is not a\
 prime number" % i
            return
    print "The given number '%d' is a prime number" % num


if __name__ == '__main__':
  num = int(input("Enter a number:"))
  is_prime_num(num)
