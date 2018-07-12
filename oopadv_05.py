#枚举类

from enum import Enum,unique

Month=Enum('Month',('Jan','Feb','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
#Month是一个类（枚举类），而Jan等都是其实例

@unique#decorator，保证无重复值
class Weekday(Enum):
    Sun,Mon,Tue,Wed,Thu,Fri,Sat=0,1,2,3,4,5,6
#下面打印枚举类的实例和值
for name,member in Weekday.__members__.items():
    print(name,'is',member,', whose value is',member.value)

#实例是Weekday.Sun等，实例的属性（value）为Weekday.Sun.value

#将Student的gender属性改为枚举类型，避免使用字符串（这个例子我不明白）
class Gender(Enum):
    Male=0
    Female=1

class Student(object):
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender