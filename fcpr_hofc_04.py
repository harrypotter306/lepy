#埃氏算法得到全体素数，采用filter函数
def odd_series():        #生成以3开头的奇数序列
    n=3
    while True:
        yield n
        n=n+2

def deduce(n):           #x对n取余，这个函数不是很理解，lambda中还有x要传入
    return lambda x: x%n>0    #返回值是bool，lambda中的n可以直接由deduce传入
#这里的deduce函数是一个高阶函数，当调用deduce(n)时，返回值是一个函数,匿名函数lambda
#即lambda x: x%n>0，是一个闭包，且调用deduce(n)时传入的参数n将存储在闭包中

def prime(n):
    x=2
    g=odd_series()
    yield x
    while x<n:
        x=next(g)
        yield x
        g=filter(deduce(x),g)    #将x的倍数都删去
        #这里的filter将g中x的倍数删去，deduce(x)即为lamda y:y%x>0