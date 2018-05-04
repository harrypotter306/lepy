#该函数用于测试命名关键字参数，输出用户信息
#命名关键字参数可以是默认参数，如这里的gender
#调用函数时命名关键字参数必须要有参数名
#e.g. person2('SH',21,gender='M',city='Yichang')
#调用时如果使用缺省值，与默认参数的用法类似
#e.g. person2('SH',21,city='Yichang')，整个gender不用输入
def person2(name,age,*,gender='M',city):
    print('name:',name,'\n''age:',age,'\n''gender:',gender,'\n''city:',city)