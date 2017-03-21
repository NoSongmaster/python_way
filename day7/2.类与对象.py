#liuhao

class Garen:
    camp='Demacia'
    def __init__(self,nickname,aggresivity,life_value):
        self.nickname=nickname
        self.aggresivity=aggresivity
        self.life_value=life_value

    def attack(self,enemy):
        print('is attacting')

#类的第一个功能：实例化
g1=Garen('草丛伦',82,100)
#类的的第二个功能：属性引用，包含数据属性和函数属性
g1.attack(2222)
#对于一个实例来说，只有一个功能：属性引用,实例本身只拥有数据属性
print(g1.nickname)
print(g1.aggresivity)
print(g1.life_value)




