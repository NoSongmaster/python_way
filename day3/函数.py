#liuhao
#函数的特性
'''
1、减少重复代码
2、使程序变的可扩展
3、便于维护
'''
def sayhi(name):
    print("hello %s"%name)
sayhi('alex')
sayhi('memu')

#实参：alex,memu 有确定值的参数，所有的数据类型都可以被当作参数传递给函数
#形参：name 只有在被调用时才分配内存，   调用结束后，立刻释放内存。值仅仅在函数内部有效(局部变量)
#形参的作用域，只在当前函数内部
'''
'''
# def change(n):
#     print(n)    #引用的全局变量
#     n="changed by func" #局部变量
#
# n='test'        #全局变量
# change(n)
# print(n)

'''
局部变量：作用域只在当前函数内部，外部变量默认不能被函数内部修改，只能引用。
如果想在函数里修改全局变量，必须global，但是强烈的建议不要这样用。
'''
#函数引用全局变量
def change():
    print(n)
n="test123"
change()

#函数内部修改全局变量
def change():
    global n
    n="changed by func"
    print(n)
n="test123"
change()
print(n)

'''
函数内部是可以修改列表，字典，集合，实例
原因，函数内部调用的内存地址是没有发生改变的。但是列表内存地址的指向元素，元素也是存入到其它内存地址的。
'''
def change():
    names[0]='Mac' #函数内修改全局的列表
    pp['age']=22
names=['alex','rain']
pp={'name':"alex"}
print(id(names),id(names[0]))       #id查看内存编号
change()
print(id(names),id(names[0]))
print(names)
print(pp)

'''
位置参数，按顺序执行
默认参数，必须放在位置参数后面
关键参数，必须放在位置参数后面  age=22
非固定参数，*args =() 以位置参数的形式传入， **kwargs={} 以关键参数形式传入。
'''


def stu_register(name, age, country, course='python_devops',*args,**kwargs):#前面是位置参数，最后面是默认参数，
    #*args是有位置参数传入的
    print("----注册佳佳幼儿园大班信息------")
    print("姓名:", name)
    print("age:", age)
    print("国籍:", country)
    print("课程:", course)
    print(args)
    print(kwargs)
#"小个子"属于不固定参数中的位置参数，所以传入到args中下面addr为关键参数，必须放到位置参数的后面。由于函数内没有addr所以会传入到kwargs中。
stu_register("贺山炮", 22, "CN", "python_devops",'小个子',addr='北京市')
stu_register("贺磊叫春", 21, "CN", "linux")



