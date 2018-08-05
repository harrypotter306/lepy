#本程序试验@property装饰器，将类方法变为属性调用
#优点：形式上保留了直接调用属性，在类定义的内部又可以方便编写参数检查等功能
#与函数式编程中的decorator用法类似（这里不明白）
class Student(object):

    @property                 #将get_score方法变为属性,在外部直接写s.score即可获得属性值
    def score(self):
        return self._score
    
    @score.setter             #第二个装饰器,将set_score方法变为属性,在外部直接写s.score=80就可以设置属性
    def score(self,value):    #实现参数检查
        if not isinstance(value,int):
            raise ValueError('score must be an integer')
        elif value<0 or value>100:
            raise ValueError('score must in the range of 0-100')
        else:
            self._score=value

class staff(object):
    @property
    def birth(self):
        return self._birth
    
    @birth.setter
    def birth(self,value):
        self._birth=value
    
    @property                 #只定义了@property方法，仅实现getter功能，只读属性
    def age(self):
        return 2018-self._birth

class screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self._width=value

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        self._height=value
    
    @property                 #这里很不明白，只用@property不用@.setter，返回值的表达式中的变量不能是新的？
    def resolution(self):     #reply：也可以是新的，但逻辑上就有问题了，原因很简单，一个属性要先设置才有值可以返回
        return self._width*self._height  #如果直接设置成新的变量，没有设置值，那就无法返回