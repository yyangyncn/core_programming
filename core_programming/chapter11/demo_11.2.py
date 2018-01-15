# 使用函数装饰器的例子
from time import ctime, sleep

def tsfunc(func):
    def wrappedFunc():
        func()
        print('[%s] %s() called' % (ctime(), func.__name__))
        return func
    return wrappedFunc

@tsfunc
def foo():
    print('invoke in foo()')

foo()