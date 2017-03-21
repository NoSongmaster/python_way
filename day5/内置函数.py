#liuhao
#将不可变的字符串，转换为可以通过ascii码修改的
bytearray()
#是否可以调用
callable('a')
#转换为asccii
chr(15)
#16进制
hex(10)
oct(1)
ord('o')
#浮点
float()
#exec将字符串形式的代码解析并执行
a="print('123')"
exec(a)
#eval将表达式的字符串形式的表达式进行运算
b='1+2-3*9'
eval(b)
#解释器使用，import实现底层
#compile()
#compile    把一个代码文件加载进来，按exec,or,eval的方式解析并执行。
f = open("函数递归.py")
data =compile(f.read(),'','exec')
exec(data)
dict()#字典
#查看对象的方法
dir()
#返回余数和商
divmod()
#filter 过滤函数返回值  打印大于5的值
a=range(10)
b=filter(lambda  x:x>5,a)
for i in b :print(i)
#map 对返回值进行操作
a=map(lambda x:x*x,range(10))
for i in a :print(i)
#reduce
from functools import reduce
a=reduce(lambda x,y:x+y,range(10))
print(a)
print(list(range(10)))
#字符串格式化
format()
#将数据变成只读。
a={1,2,4,34,3,3}
frozenset(a)
#globals() #将当前程序在内存中所有全局变量都以字典的形式打印出来。
globals()
#locals() 将当前程序在内存中所有局部变量以字典的形式大于出来
locals()
#hash() #保证字符在当前程序下是唯一的。
hash('alex')
#iter()

#memoryview()
#在进行切片并赋值数据时，不需要重新copy原列表数据，可以直接映射原数据内存。
#对比，直接修改内存地址，修改变量和赋值修改变量。
import time
for n in (100000, 200000, 300000, 400000):
    data = b'x'*n
    start = time.time()
    b = data
    while b:
        b = b[1:]
    print('bytes', n, time.time()-start)

for n in (100000, 200000, 300000, 400000):
    data = b'x'*n
    start = time.time()
    b = memoryview(data)
    while b:
        b = b[1:]
    print('memoryview', n, time.time()-start)

#print()进度条
import time
for i in range(10):
    print('#',end='',flush=True)
    time.sleep(0.5)
#print 写入文件
f=open("file.txt",'w',encoding='utf-8')
print("hey",file=f)
f.close()
#repr，返回字符串。转换为字符串形式
def hey():pass
a=repr(hey)
#反转reversed
a=[1,2,3,4]
print(reversed(a))
#round 保留几位小数
a=3.12384945
round(a,2)
#sice,切片.规定一个切片格式。
a=range(20)
pattern=slice(3,8,2)
for i in a[pattern]:
    print(i)
#sorted

#vars 将所有的变量打印出来
#zip  #拉链
a=list(range(10))
b=list(range(10,16))
print(zip(a,b))

#__import__()
#导入用户输入的模块,用户输入是字符形式
__import__("123")