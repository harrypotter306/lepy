#该例子用来说明可变参数，计算传入所有数字的平方和
#传入的数据将被自动组装为一个tuple
#(1)可以传入任意数量的数字，调用格式为squsum(1,2,3)
#(2)可以传入一个list或tuple，调用格式为squsum(*listname)
def squsum(*num):
    sum=0
    for n in num:
        sum=sum+n*n
    return sum