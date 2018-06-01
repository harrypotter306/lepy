#!/user/bin/env python
#-*- coding utf-8 -*-

' a test module '

__author__='Harry Potter'              #__author__是一个特殊变量

import sys

def test():
    args=sys.argv
    if len(args)==1:
        print('Hello, World!')
    elif len(args)==2:
        print('Hello, %s' % args[1])
    else:
        print('Too many arguments!')

def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):                  #这两个函数名是非公开的，亲测也是可以引用的
    return 'Hi, %s' % name

def greeting(name):
    if len(name)>3:
        return _private_1(name)
    else:
        return _private_2(name)

if __name__=='__main__':               #这个if条件句和__name__用于在命令行中测试
    test()                             #命令行执行改模块, 会把'__main__'赋值给__name__变量.

#这个模块是自己编写的，主要看一下一般模块的格式，运行检测的方法，三种变量作用域