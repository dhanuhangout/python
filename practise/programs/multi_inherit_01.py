
class ClassA(object):
    def __init__(self):
        super(ClassA, self).__init__()
        print 'Class A constructor.'
        self.a = 5

class ClassB(ClassA):
    def __init__(self):
        super(ClassB, self).__init__()
        print 'Class B constructor.'
        self.b = 6

class ClassC(ClassB):
    def __init__(self):
        super(ClassC, self).__init__()
        print 'Class C constructor.'
        self.c = 7
        self.obj_d = self.ClassD(self)
        self.obj_d.func1()

    def invoke_func2(self):
        self.obj_d.func2()

    def c_func(self):
        print 'c func'

    class ClassD(object):
        def __init__(self, classc_obj):
            # super(ClassD, self).__init__()
            self.classc_obj = classc_obj
            self.obj_e = ClassE(self.classc_obj.c)

        def func1(self):
            print 'func1, c'

        def func2(self):
            print 'func2'
            self.classc_obj.c_func()


class ClassE(object):
    def __init__(self, obj):
        print 'ClassE'
        self.obj = obj
        print obj


if __name__ == '__main__':
    print 'Start.'
    temp_obj = ClassC()
    print temp_obj.a
    print temp_obj.b
    print temp_obj.c
    temp_obj.invoke_func2()
    print 'End.'

# OUTPUT:
'''
$ python multi_inherit_01.py 
Start.
Class A constructor.
Class B constructor.
Class C constructor.
5
6
7
End.
'''

