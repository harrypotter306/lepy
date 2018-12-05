#在当前目录及当前目录的所有子目录下找到指定的类型的文件
import os
#P=os.path.abspath('.')   #current absolute directory
#------------This file is not perfect------------
#some file has no extension just like folders
def searchfile(fs,P=os.path.abspath('.')):     #fs is the item of files, for example, '.py'
    #default directory is current directory
    f=[]
    for x in os.listdir(P):
        if os.path.splitext(x)[1]==fs:
            f.append(x)
            print(x)
        elif os.path.isdir(os.path.join(P,x)): #os.path.splitext(x)[1]=='':
            p=os.path.join(P,x)
            searchfile(fs,p)    