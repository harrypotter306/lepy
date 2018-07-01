#first oop program
class Student(object):
    na='Student'                         #类属性
    def __init__(self,name,score):       #实例属性
        self.name=name
        self.__score=score
    
    def read_score(self):
        return self.__score
    
    def reset_score(self,score):
        if 0<=score<=100:
            self.__score=score
        else:
            print('Error Score Type')
    
    def get_grade(self):
        if self.__score>=90:
            return 'A'
        elif self.__score>=80:
            return 'B'
        else:
            return 'c'
    
    def print_score(self):
        print('%s\'s score is %s' % (self.name,self.__score))