#liuhao

name="my name is alex"
#首字母大写
print(name.capitalize())
#统计字符的个数
print(name.count('a'))
#一共打印50个字符，不够的用#补全
print(name.center(50,'#'))
#ljust，rjust.定义50个字符，不够的填充
print(name.ljust(50,'*'))
print(name.rjust(50,'*'))
#设置\t距离为多少个字符
a="a\tb"
print(a.expandtabs(30))
#find,获取字符的位置
print(name.find("is"))
print(name[0:name.find("is")])
#format格式化输出
a="this is {name},he is {age}"
print(a.format(name="alex",age=33))
#字典格式化输出
print(a.format_map({'name':'liuhao','age':'23'}))
#判断结尾是不是ex，返回布尔值
print(name.endswith("ex"))
#判断是否为数字+字母。不能有特殊字符。返回布尔值
print('2222'.isalnum())
#判断只为字符，
print("abA".isalpha())
#判断是不是一个整数,常用
print("2222".isdigit())
#判断是不是一个合法的标识符，字符和_开头
print('d77sss'.isidentifier())
#判断为小写
print('a'.islower())
#判断是不是每个首字母大写
print("I Am Is".istitle())
#字符串join用法,用前面的填充后面的
print("666is ".join("===="))
print('+'.join(['1','2','3']))
#全部变小写，全部变大写
print('Alex'.lower())
print('Alex'.upper())
#去掉左边的换行符，lstrip#rstrip去掉右边的换行符
print('\nAlex'.lstrip())
print('-------')
#去掉两边的换行符strip()
#编码，
p=str.maketrans("abcdef",'123456')
print("alex li".translate(p))
#replace替换,将l替换为L,只替换一个
print('alex li'.replace('l','L',1))
#rfind找到最后一个值得下标返回
print('alex lil'.rfind('l'))
#分割，将字符串分割为列表,默认为空格
print('al ex dd li l ss'.split())
print('1+2+3+4'.split('+'))
#字符串大小写转换
print('Alex Li'.swapcase())


