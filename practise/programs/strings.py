'''Strings demo.'''
print
print "***** Given Strings ****"
STR1 = "          3333333this is STR1 string333333          "
STR2 = "string2"
print "STR1 = '%s'" % STR1
print "STR2 = '%s'" % STR2

print
print "***** String Methods *****"
print "STR1.lower() = '%s'" % STR1.lower()
print "STR1.upper() = '%s'" % STR1.upper()
print "STR1.lstrip() = '%s'" % STR1.lstrip()
print "STR1.rstrip() = '%s'" % STR1.rstrip()
print "STR1.strip(\" 3\") = '%s'" % STR1.strip(" 3")
print "STR1.swapcase() = '%s'" % STR1.swapcase()
print "\",\".join(STR2) = '%s'" % ",".join(STR2)
print
