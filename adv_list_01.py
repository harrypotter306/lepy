#测试列表生成式
#将输入的list中所有字符串大写转为小写
#对于非字符型变量，不改变
def smstr(L):
    s=[a.lower() if isinstance(a,str) else a for a in L]
    return s