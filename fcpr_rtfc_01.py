#返回函数counter，每次调用结果+1
#测试返回函数
#我个人觉得这个功能用generator可以直接得到，而且节省内存
def CreatCounter():
    i=[0]                  #这里利用了list是全局变量？
    def counter():
        i[0]+=1
        return i[0]
    return counter
#ca=CreatCounter()，调用了高阶函数CreatCounter,得到i=[0]（全局变量不释放）
#且ca=counter
#调用ca，即ca()，则不断在counter内部进行计算，由于i是list不释放，所以结果累加。