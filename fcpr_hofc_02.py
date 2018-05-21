#本程序实现将输入的一串名字转换为首字母大写，其他字母小写的格式
#需要使用map高阶函数
def nor(L):
    def mal(name):
        if len(name)==1:
            n=name.upper()
        else:
            n=name[0].upper()+name[1:].lower()
        return n
    Ln=list(map(mal,L))
    return Ln