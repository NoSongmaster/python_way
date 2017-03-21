#liuhao


def func(x:int,y:int)->int:
    pass
print(func.__annotations__)

#从实参的角度，
def foo(x,y):
    print(x,y)
#按位置
foo(1,2)
#按key=value关键字形式
foo(y=2,x=1)
#针对同一个形参，我们要么按照位置要么按照关键字为形参传值。
#foo()

#foo(y=2,1) #错误
#从形参的角度：位置参数，默认参数，可变长参数，**kwargs
def foo(x,y,z):#位置参数：必传参数
    print(x,y,z)

#默认参数
def foo(x,y=1):
    print(x,y)
foo(1)
# 可变长参数 *args
def foo(x,y,*args):
    print(x,y,args)

#foo(1,2,3,4,5,6,7)
l=['a','b']
foo(1,2,*l) #*args的形式就等于1，2，3，4


def foo(x,y,z):
    print(x,y,z)
#foo(1,2,3)
l=[1,2,3]
foo(*l)#*默认分别去取l中的元素，按位置传给foo

def foo(x,**kwargs):
    print(x)
    print(kwargs)
foo(1,y=3,z=1)
dic={'a':1,'b':2}
foo(1,**dic)    #foo(1,a=1,b=2)

def foo(x,y,z):
    print()

'''
*sym 等同于 展开按照位置的方式
**args 等同于 展开按照关键字
'''













