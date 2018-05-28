#埃氏算法得到全体素数，采用filter函数
def odd_series():        #生成以3开头的奇数序列
    n=3
    while True:
        yield n
        n=n+2

def deduce(n):           #x对n取余，这个函数不是很理解，lambda中还有x要传入
    return lambda x: x%n>0    #返回值是bool，lambda中的n可以直接由deduce传入

def prime(n):
    x=2
    g=odd_series()
    yield x
    while x<n:
        x=next(g)
        yield x
        g=filter(deduce(x),g)    #将x的倍数都删去