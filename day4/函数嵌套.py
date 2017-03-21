#liuhao

#嵌套调用
def my_max4(a,b,c,d):
    res1=my_max2(a,b)
    res2 = my_max2(res1, c)
    res3 = my_max2(res2, d)
    return res3

def my_max2(x,y):
    if x> y:
        return x
    else: return y

print(my_max4(100,2,343,121))
#嵌套定义
def fun1():
    def fun2():
        print(1)
    return fun2


