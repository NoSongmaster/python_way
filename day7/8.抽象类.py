#liuhao
import abc
class ALLFile(metaclass=abc.ABCMeta):  #抽象类
    @abc.abstractmethod      #加这个装饰器的必须在子类中实现
    def read(self): #
        pass
    @abc.abstractmethod     #加这个装饰器的必须在子类中实现
    def write(self):
        pass
    def test(self):#可以不被实现
        print('22222222')
class Text(ALLFile):    #子类中必须实现父类中规定的两个方法
    def read(self):pass
    def write(self):pass
t1=Text()
t1.test()
# 抽象类不能被实例化，
# a=ALLFile()