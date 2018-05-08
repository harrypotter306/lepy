#这个程序实现汉诺塔的移动，输出移动的步骤
#完成n个板的移动需要3步：
#1.把上面n-1个板移到b；
#2.把a最下面的板子移到c；
#3.把b的n-1个板子移到c。
def hanoi(n,a,b,c):     #全功能是n个盘从a到c
    if n==1:
        print('move',a,'-->',c)
    else:
        hanoi(n-1,a,c,b)
        #hanoi(1,a,b,c)
        print('move',a,'-->',c)     #这一步和上面注释中的一步效果相同
        hanoi(n-1,b,a,c)