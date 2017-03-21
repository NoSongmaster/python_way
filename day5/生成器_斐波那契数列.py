#liuhao
#除了第一个和第二个数，任意一个数都可由前两个数相加得到:
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        #t=a+b
        #a=b
        #b=t
        a, b = b, a + b
        n = n + 1
    return 'done'
f=fib(15)
#将函数转换为生成器,yield
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
#此时yield  已经将函数变成了生成器
# f=fib(10)
# print(f)
# #在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print("可以在函数执行过程中做点别的事情")
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
for i in fib(100):
    print(i)
