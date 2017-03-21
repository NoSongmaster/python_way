#liuhao
class A:    #默认继承object
    pass
class B(A):#继承A
    pass
#打印继承的父类
print(B.__bases__)  #继承了
print(A.__bases__)  #

#新式的类
class Animal:

    start='earth'
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def run(self):
        print('running')
    def talk(self):
        print('talking')
class People(Animal):
    pass
    def piao(self):
        print('大保健')
class Pig(Animal):
    pass

p1=People('alex',50,'F')
pig1=Pig('贺磊',250,'22')
print(p1.start)
p1.run()
#继承可以重用代码
class Hero:
    def __init__(self,nickname,aggresivity,life_value):
        self.nickname=nickname
        self.aggresivity=aggresivity
        self.life_value=life_value

    def attack(self,enemy):
        print('is attacting',enemy.nickname)
        enemy.life_value-=self.aggresivity
class Garen(Hero):
    camp='Demacia'

class Riven(Hero):
    camp='Noxus'