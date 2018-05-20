#本程序是函数式编程第一个程序
#本程序主要试验高阶函数部分的map和reduce函数
#利用map和reduce函数实现字符串转为数值，即str2num
from functools import reduce

def str2num(s):
    D={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    #这个dict放在函数外面为何也可以？import这一句在函数外面是起作用的，什么原理？
    def num1(x):       #函数内部定义函数，参数名可以是相同的，这里也可以是s
        return D[x]
    def num2(a,b):
        return 10*a+b
    return reduce(num2,map(num1,s))