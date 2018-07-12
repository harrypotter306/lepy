#本文件是class中一些特别的定制方法，如slots类型的
class Student(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):#print一个实例时，得到__str__的返回值
        return 'Student object (name, %s)' % self.name
    def __repr__(self):#直接输入实例名时，得到__repr__的返回值
        return 'Student object(for builder)'
    #通常简化写法：__repr__=__str__(二者内容一样)

class Fib(object):
    def __init__(self):
        self.a,self.b=0,1
    def __iter__(self):#返回值为实例自身
        return self
    def __next__(self):#for循环不断调用__next__的返回值，直到StopIteration
        self.a,self.b=self.b,self.a+self.b
        if self.a>1e5:
            raise StopIteration()
        return self.a

class Fib2(object):
    def __getitem__(self,n):
        if isinstance(n,int):#传入的参数是int
            a,b=0,1
            for x in range(n):
                a,b=b,a+b
            return a
        if isinstance(n,slice):#传入的参数是切片
            start=n.start
            stop=n.stop
            if start is None:
                start=0
            a,b=0,1
            L=[]
            for x in range(stop):
                if x>=start:
                    L.append(a)
                a,b=b,a+b
            return L

class Student2(object):
    def __init__(self):
        self.name='Abc'
    def __getattr__(self,ater):#若实例的属性为score，可以赋值为99
        if ater=='score':
            return 99
        else:
            raise AttributeError('Error')

class Student3(object):
    def __init__(self,name):
        self.name=name
    def __call__(self):
        print('My name is %s' % self.name)
