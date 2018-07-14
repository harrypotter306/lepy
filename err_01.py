#handle the error
#part 1
try:
    print('trying...\nplease input a number')
    a=input()
    r=10/int(a)
    print('result',r)
except ValueError as e:
    print('ValueError:',e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:',e)
else:
    print('no error')
finally:
    print('finally')
print('End')

#part 2
