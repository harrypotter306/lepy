#本程序测试sorted函数，其中主要是关键字key的使用
#sorted函数使用关键是构造key传入的函数
#本程序将name-grade对按照成绩排序，再按照姓名首字母排序，不区分大小写
def paxu(L):
    def p_grade(t):
        return t[1]
    def p_name(t):
        return t[0].lower()    #注意这里有()，如果没有()结果不对
    Lp=sorted(sorted(L,key=p_name),key=p_grade,reverse=True)
    return Lp