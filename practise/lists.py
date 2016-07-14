print "***** List operations *****"
list_obj1 = [1, 2, 1, 2, 3]
list_obj1_dup = [1, 2, 1, 2, 3]
list_obj2 = [4, 5, 6, 7, 8]
list_obj3 = [3, 2, 1, 2, 1]
list_obj4 = [0, 9, 8, 7, 6]
tuple_obj = ('a', 'b', 'c', 'd', 'e')

print
print "***** Given lists *****"
print "list_obj1 = ", list_obj1
print "list_obj2 = ", list_obj2
print "list_obj3 = ", list_obj3
print "list_obj4 = ", list_obj4
print "list_obj1_dup = ", list_obj1_dup

print
print "***** List Indexing *****"
print "list_obj1[0] = ", list_obj1[0]
print "list_obj1[4] = ", list_obj1[4]
print "list_obj1[-1] = ", list_obj1[-1]
print "list_obj1[-4] = ", list_obj1[-4]

print
print "***** List slicing *****"
print "list_obj1[:] = ", list_obj1[1:]
print "list_obj1[:3] = ", list_obj1[:3]
print "list_obj1[2:] = ", list_obj1[2:]
print "list_obj1[2:4] = ", list_obj1[2:4]

print
print "***** List Methods *****"
print "list_obj1.count(1) = ", list_obj1.count(1)
print "list_obj1.index(3) = ", list_obj1.index(3)
list_obj2.append(9)
print "list_obj2.append(9) = ", list_obj2
list_obj2.reverse()
print "list_obj2.reverse() = ", list_obj2
list_obj2.sort()
print "list_obj2.sort() = ", list_obj2
list_obj2.extend(tuple_obj)
print "list_obj2.extend(tuple_obj) = ", list_obj2
list_obj2.remove(8)
print "list_obj2.remove(8) = ", list_obj2
list_obj2.pop(-4)
print "list_obj2.pop(-4) = ", list_obj2
list_obj2.sort()
print "list_obj2.sort() = ", list_obj2

print
print "***** List Functions *****"
print "len(list_obj4) = ", len(list_obj4)
print "max(list_obj4) = ", max(list_obj4)
print "min(list_obj4) = ", min(list_obj4)
print "cmp(list_obj1, list_obj1_dup) = ", cmp(list_obj1, list_obj1_dup)
print "list(tuple_obj) = ", list(tuple_obj)

print
print "***** List Operations *****"
print "list_obj1 '+' list_obj2 = ", (list_obj1+list_obj2)
print "list_obj1 '*' 2 = ", (list_obj1*2)
