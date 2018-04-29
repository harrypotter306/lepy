#本程序尝试python中的if-else语句
#首先判断是否是数值型数据（整数和浮点）
#是则返回绝对值，不是打印typeerror，无返回值
def my_abs(x):
    if isinstance(x,(int,float)):
        if x>=0:
            return x
        else:
            return -x
    else:
        print('TypeError: bad operand type')
