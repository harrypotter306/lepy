class Student(object):
    names='xuesheng'#类属性
    def get_name(self):
        print(0)

s=Student()
s.name='wjw'
#dir()对对象（类和实例）都可以操作
dir(s)
dir(Student)
#hasattr()对对象（类和实例）都可以操作
hasattr(s,'names') #True类属性
hasattr(s,'name')  #True实例属性
hasattr(s,'get_name')  #True类方法
hasattr(Student,'names') #True类属性
hasattr(Student,'name')  #False实例属性
hasattr(Student,'get_name') #True类方法
