#liuhao
# class A:
#     def test(self):
#         print('from A.test')
# class B(A):
#     def test(self):
#         A.test(self)
#         print('B.test')
# b1=B()
# b1.test()
class People(object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
class Teacher(People):
    def __init__(self,name,age,sex,level):
        #People.__init__(name,age,sex)  #需要知道父类的名字~
        super().__init__(name,age,sex)  #推荐用法
        self.level=level
t1=Teacher('alex',22,'m','高级')
print(t1.name)


