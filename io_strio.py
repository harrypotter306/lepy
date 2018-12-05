#Recording the use of StringIO & BytesIO
from io import StringIO
f=StringIO('Hello, world!\nMy name is Harry.\nNice to meet you!')
while True:
    s=f.readline()
    if s=='':
        break
    print(s.strip())  #s.strip()去除首尾的制定字符，默认是空格或换行

from io import BytesIO
fb=BytesIO('中文'.encode('utf-8'))
print(fb.getvalue())