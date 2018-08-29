#debug
# (1)assert
def foo(s):
    a=int(s)
    assert a!=0,'s is zero'
    return 10/a
def main():
    s=input()
    print(foo(s))
    return foo(s)
main()

#(2)logging
import logging
logging.basicConfig(level=logging.INFO)
s2=input()
a2=int(s2)
logging.info('a2=%d' % a2)
print(10/a2)

#(3)pdb
import pdb
s3='4'
a3=int(s3)
pdb.set_trace()
print(10/a3)
a3=a3+10
pdb.set_trace()
print(10/a3)