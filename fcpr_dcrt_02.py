#构造一个decorator，对于任何定义的新函数，都可以返回当前时间
import functools,time
def log(func):
    @functools.wraps(func)
    def wrapper(*arg,**kw):
        t=time.asctime(time.localtime(time.time()))
        print('%s is excuted at %s' % (func.__name__,t))
        return func(*arg,**kw)
    return wrapper