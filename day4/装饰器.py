#liuhao
'''
装饰器：在遵循下面两个原则的前提下为被修饰者添加新功能
必须遵循两个原则
1、一定不能修改源代码
2、不能修改调用方式
'''

#装饰器
# def timer(func):
#     def wrapper():
#         pass
#     return wrapper
#
#
# #获取index的执行时间
# @timer #index=timer(index)
# def index():
#     print('in the index')

# @deco2
# @deco1  #func1=deco1(index)--> func2=deco2(func1)
# def index():
#     print('in the index')
import time
def timer(func):
    def wrapper(*args,**kwargs):    #'tom','xxxx'--->
        start_time=time.time()
        print(args)
        res=func(*args,**kwargs)    #这里是传入函数执行
        stop_time=time.time()
        print('run time is %s'%(stop_time-start_time))
        return "123"    ##加完装饰器的函数，返回值在这里定义
    return wrapper

@timer  #index=timer(index)
def index(msg):
    print('this is index ',msg)

print(index('sasa'))

#有参装饰器
# @timer(type='xxx')  #先执行一下装饰器，返回值res. res=time(type='xxx),@res
# def home():
#     pass