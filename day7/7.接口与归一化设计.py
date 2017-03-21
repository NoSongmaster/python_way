#liuhao


#接口的概念，父类只写名字，不写实现
class ALLFile:  #接口类
    def read(self): #接口函数
        pass
    def write(self):
        pass
class Text(ALLFile):    #子类继承父类
    def read(self):
        print('text read')
    def write(self):
        print('text write')
class Sata(ALLFile):    #子类继承父类
    def read(self):
        print('sata read')
    def write(self):
        print('sata write')
t=Text()
s=Sata()
t.read()
t.write()
s.read()
s.write()



