#本程序用于实验decorator装饰器，包括执行的部分
def log(text):
    def decorator(func):
        def wrapper(*arg,**kw):
            print ('%s %s()' % (text,func.__name__))
            return func(*arg,**kw)
        return wrapper
    return decorator

@log('excute')
def now():
    print('2018-05-29')

now()
print(now.__name__)
#运行说明：
#(1)首先定义装饰器log（本质上是一个返回函数的高阶函数）
#(2)执行@log('excute')，并定义函数now
#相当于定义函数now，并执行了now=log('excute')(now)
#本质上是定义的函数now当作参数传入了log函数的返回值decorator函数，now的内容已改变
#(3)执行@log('excute')即now=log('excute')(now)
#log('excute')返回decorator，故为now=decorator(now)，返回wrapper，即now=wrapper
#最后调用now()（这已经不是最初定义的now了），而是做了wrapper()
#因此先print然后返回now()（注意wrapper是闭包，之前传入的参数都保留了）