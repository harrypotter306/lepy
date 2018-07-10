#多重继承
#0顶端，父类
class Animal(object):
    def intro(self):
        print('Not Human')

#1Mammal和Bird继承Animal
class Mammal(Animal):
    pass

class Bird(Animal):
    pass
#以上为单一继承的主线

#定义多重继承的类Runnable和Flyable，可以同时继承，获得更多的方法
class Runnable(object):
    def run(self):
        print('I can run')

class Flyable(object):
    def fly(self):
        print('I can fly')

#2Dog和Bat继承Mammal，同时，Dog属于Runnable，Bat属于Flyable
class Dog(Mammal,Runnable):
    pass
class Bat(Mammal,Flyable):
    pass

#2Parrot和Ostrich继承Bird，同时，Parrot属于Flyable，Ostrich属于Runable
class Parrot(Bird,Flyable):
    pass
class Ostrich(Bird,Runnable):
    pass