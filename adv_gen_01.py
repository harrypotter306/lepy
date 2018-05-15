#利用生成器generator生成杨辉三角
#每次输出杨辉三角的一行，为一个list
def triyh(n):
    L=[1]
    x=0
    while x<n:
        yield L
        L.insert(0,0)          #这里采用的算法是在list的最前面加一个0
        i=0                    #然后用L[i]和L[i+1]相加,作为L[i]
        while i<len(L)-1:      #这样新的L[i]不会覆盖旧的L[i+1]
            L[i]=L[i]+L[i+1]   #反过来，用i-1元素加i元素是不行的
            i=i+1              #一定要注意list是可变对象，   
        x=x+1                  #给变量赋值是把变量名指向一个常量