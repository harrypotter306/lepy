#this file is built for advanced oop
#part1 __slots__
class Student(object):
    __slots__=('name','age')

class Undergraduate(Student):
    __slots__=('score','set_gender')
    #这里的set_gender可以在外部通过MethodType绑定给Undergraduate的实例(如su)
    #但是绑定之后, 调用su.set_gender('M')，会报错，因为__slots__不含'gender'

class Master(Student):
    pass