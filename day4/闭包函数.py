#liuhao
#内部函数对外部函数参数的调用。。注意是外部函数。
def f1():
    x=1
    def f2():
        print(x)
    return f2
