#本程序实现把输入的内容为浮点数的字符串转换为浮点数
#利用map和reduce函数
from functools import reduce
D={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def str2float(s):
    def str2char(ss):
        return D[ss]
    def fn(x,y):
        return 10*x+y
    Li=[]
    i=0
    for x in s:
        if x!='.':
            i=i+1
            Li.append(x)
        else:
            break
    Lf=list(s[i+1:])      #循环结束，分别得到整数部分和小数部分的list
    f=reduce(fn,map(str2char,Li))+reduce(fn,map(str2char,Lf))/10**len(Lf)
    return f