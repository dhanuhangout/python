print "***** Given Dictionaries ****"
dict_obj1 = {
    'Name': 'Zara',
    'Age': 7,
    'Class': 'First'
}

dict_obj2 = {
    'Name': 'Test',
    'Age': 3,
    'Class': 'Dev'
}

dict_obj3 = {
    'Name': 'Zara',
    'Age': 7,
    'Class': 'First'
}

dict_obj4 = { }

tup_obj = ('Name', 'Age', 'Class')

print "***** Accessing Dictionary values *****"
print "dict_obj1['Name'] = '%s'" % dict_obj1['Name']
print "dict_obj1['Age'] = '%s'" % dict_obj1['Age']
print "dict_obj1['Class'] = '%s'" % dict_obj1['Class']

print "***** Updating & Adding Dictionary elements *****"
dict_obj1['Age'] = 8
dict_obj1['School'] = 'DPS School'

print "dict_obj1['Age'] = '%s'" % dict_obj1['Age']
print "dict_obj1['School'] = '%s'" % dict_obj1['School']

print "***** Properties of Dictionary Keys *****"
print "* No duplicate key is allowed."
print "* Strings, number or tuples can be used as keys. But ['key'] not allowed"


print "***** Build-in Functions *****"
print "cmp(dict_obj1, dict_obj3) = %s" % cmp(dict_obj1, dict_obj3)
print "len(dict_obj1) = %s" % len(dict_obj1)
print "str(dict_obj1) = %s" % str(dict_obj1)

print "***** Build-in Methods *****"
print "dict_obj1.items = %s" % dict_obj1.items
print "dict_obj1.values = %s" % dict_obj1.values
print "dict_obj1.keys = %s" % dict_obj1.keys
print "dict_obj1.has_key('Name') = %s" % dict_obj1.has_key('Name')
# print "dict_obj4.copy(dict_obj1)" % dict_obj4.copy(dict_obj1)
print "dict_obj4.udpate(dict_obj2) = %s" % dict_obj4.update(dict_obj2)
print "dict_obj4.get('Name') = %s" % dict_obj4.get('Name')
print "dict_obj4.setdefault('Height', None) = %s" % dict_obj4.setdefault('Height', None)
# print "dict_obj4.clear = %s" % dict_obj4.clear
print "dict_obj4.fromkeys(tup_obj) = %s" % dict_obj4.fromkeys(tup_obj, 10)


print "***** Deleting Dictionary elements *****"
# print "del dict_obj4['Name'] = %s" % $(del dict_obj4['Name'])
# print "dict_obj4.clear() = %s" % dict_obj4.clear()
# print "del dict_obj4" % (del dict_obj4)
