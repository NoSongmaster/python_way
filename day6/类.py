#liuhao
class Dog(object):
    age=22  #类变量，存在类的内存地址里，可以被所有实例共享引用
    def __init__(self,name,type):   #初始化函数（构造函数）
        self.name=name
        self.type=type
    def balk(self):
        print('%s is a dog'%self.name)

d=Dog('贺磊','牧羊犬')
print(d.name,d.type)
d.balk()

'''
面向对象中：函数叫做方法
类变量:
    作为默认公有属性
    全局修改或增加新属性
实例变量(成员属性)
    每个实例存在自己内存空间里的属性
公有属性==类变量

私有属性
    __sex   代表私有属性，仅能在内部各函数(方法)中调用
    隐藏一些功能的实现细节，只给外部暴露调用接口。

继承：
    1.直接调用父类方法
    2.继承父类方法并重构父类方法，先重构，在重构的方法里手动调用父类方法   重构:__init__
    3.可以定义子类自己的方法
    4.析构方法  __del__
'''
#类变量
class People():
    def __init__(self,name,age,job):
        self.name=name
        self.age=age
        self.job=job
p=People("helei",'22','it')
People.fuli='da bao jian'   #添加一个类的变量     #全局增加新属性
print(p.fuli)
p.hotjob='aaa'  #添加一个实例变量
print(p.hotjob)
#实例变量(成员属性)
class People():
    fuli='dabaojian'    #类变量，实例生成后，会生成引用关系，但是内存还是调用类的内存
    def __init__(self,name,age,job,sex):
        self.name=name  #实例变量，生成实例后存在于实例的内存空间
        self.age=age
        self.job=job
        self.__sex=sex  #私有属性，只能内部各方法中调用
    def show(self):
        print('my name is %s',self.name)
    def get_sex(self):
        print(self.__sex)
p1=People('helei','22','dd','F')
#print(p1.__sex)    #这里会报错，因为私有属性不能在外部调用，只能通过内部方法调用
p1.get_sex()#可以通过内部的方法调用


