#liuhao
a=[1,2,3,4,5,6,7,8,9,10]
# for index,i in enumerate(a):
#     a[index]=i+1
# print(a)
# 列表生成式
# a=[i+1 for i in a]
# print(a)
#将列表中大于5的全部进行幂运算
# a=[1,2,3,4,5,6,7,8,9,10]
# a=[i*i if i >5 else i for i in a]
# print(a)
#列表生成器  #边执行边运算=惰性运算
a=(i*i if i >5 else i for i in a)
print(a)
# for i in a:
#     print(i )
#提供next方法，来实现进行调用。编执行边运算
#优点，不需要提前生成大量的数据来占用内存。节省内存。不知道下一个，上一个。只能一步步往下走。不知道尽头在哪儿里
#next() 和 a.__next__() 完全一样
print(next(a))
print(next(a))
print(next(a))
print(a.__next__())
#上面的next()方法太麻烦了。
# for i in a :
#     print(i )
# for i in a :
#     print(i)





