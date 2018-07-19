#利用类属性，每创建一个实例，类属性+1
class Student(object):
    count=0

    def __init__(self,name):       #要注意到，每创建一个实例，__init__()是要执行的
        Student.count+=1           #注意一定要用Student.count而不是count,不完全理解
        self.name=name
    
    def print_name(self):
        print('my name is %s' % self.name)