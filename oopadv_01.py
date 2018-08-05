#this file is built for advanced oop
#part1 __slots__
class Student(object):
    __slots__=('name','age')
    def set_age(self,age):       #set_age是类的方法，__slots__并不限制
        self.age=age

class Undergraduate(Student):
    __slots__=('score','set_gender')
    #这里的set_gender可以在外部通过MethodType绑定给Undergraduate的实例(如su)
    #但是绑定之后, 调用su.set_gender('M')，会报错，因为__slots__不含'gender'

class Master(Student):
    pass
    #Master类没有__slots__, 所以父类的__slots__对其也没有作用