#利用for迭代，查找一个list中的最小值和最大值，并返回一个tuple
#可以看到，python中的for循环直接对元素迭代，而不需要通过下标，抽象度高
def findmm(L):
    if L==[]:
        return None
    elif len(L)==1:
        return L[0],L[0]
    else:
        mi=L[0]
        ma=L[0]
        for x in L:
            if x<mi:
                mi=x
            if x>ma:
                ma=x
        return mi,ma