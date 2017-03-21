#liuhao
import random
#在1-10中取随机数
print(random.randint(1,10))
#在1-20 步长为2中去随机数。奇数
print(random.randrange(1,20,2))
#取5个随机数
print(random.sample(range(100),5))


'''生成随机数进行验证'''
import random
checkcode = ''
for i in range(4):  #循环4次，生成4个随机数
    current = random.randrange(0,4) #从0-3中选取一个随机数
    if current != i:                #如果随机数与正在循环的次数不相等，随机一个字母
        temp = chr(random.randint(65,90))
    else:                           #相等，随机一个数字
        temp = random.randint(0,9)
    checkcode += str(temp)
print(checkcode)
'''随机验证高级精简版'''
import random,string
#string.digits 0-9的整数
# string.ascii_uppercase 大写的ascii码字符
source=string.digits+string.ascii_uppercase
#source : 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ
print("".join(random.sample(source,6)))
