#liuhao
#集合：无序的，去重的特点
#name={9,1,2,3,4,56,7,8,32,3,2,3,45,6,87}
#增加
#name.add(1)
#删除
#name.remove(22)
#print(name)

a={1,3,5,7,9}
b={2,3,4,5,6,8}
print( a & b )  #交集
print(a.intersection(b))
#将a和b的交集赋值给a
#a.intersection_update(b) #a=a.intersection(b)
print( a - b )   #差集
print( a.difference(b))
#a.difference_update(b)
print(  a | b )   #并集
print( a.union(b))
print( a ^ b )      #对称差集
print( a.symmetric_difference(b))
#a.symmetric_difference_update(b)




