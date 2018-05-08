#small practice
#对输入的所有数字做乘积
def mtpl(*fac):
    sum=1
    for x in fac:
        sum=x*sum
    return sum