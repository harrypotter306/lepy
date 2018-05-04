#该函数用来说明关键字参数，输出用户信息
#传入的关键字参数将被组装为一个dict
#(1)依次传入关键字参数的key和value，注意key不打引号，如下面的gender,age等
#e.g. person('SH',gender='M',age=21,city='Wuhan',School='HUST')
#(2)首先定义dict，在调用函数的时候用**dictname传入
#e.g. d={'gender':'M','age':21,'city':'Wuhan','school':'HUST'}
#person('SH',**d)
def person(name,**kw):
    print('name:',name,'\n''other:',kw)