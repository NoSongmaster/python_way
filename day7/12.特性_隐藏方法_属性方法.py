#liuhao
#方法->>变量
# import math
# class Circle:
#     def __init__(self,redius): #圆的半径
#         self.__redius=redius
#     @property   #mainji=property(mianji)
#     def mianji(self):   #计算圆的面积
#         return math.pi*self.__redius*self.__redius
#
# c=Circle(10)
# print(c.mianji)

class A:
    def __init__(self,name):
        self.__name=name
    @property   #将这个类中的方法，变成一个类中的属性，可以通过.name调用
    def name(self):
        return self.__name      #当调用.name时返回的是__self.name
    @name.setter    #赋值操作调用，当为.name赋值时调用
    def name(self,value):
       # print('------')
        if not isinstance(value,str):   #判断赋值的是不是字符
           raise TypeError('%s must be str'%value)#抛出异常
        self.__name=value
    @name.deleter   #删除.name属性时调用
    def name(self):
        print('=====')
        del self.__name
a=A('ennn')
print(a.name)
a.name='ssa'
print(a.name)
del a.name
