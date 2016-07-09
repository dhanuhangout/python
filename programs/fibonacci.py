#!/usr/bin/python

def fibonacci_series(num):
    if num == 0:
      return 0
    list_obj = [0,1]
    for i in range(1, num):
	j = list_obj[-1] + list_obj[-2]
	list_obj.append(j)
    return list_obj


if __name__ == '__main__':
  print "Enter a number to get fibonacci series:"
  num = int(input())
  print fibonacci_series(num)
