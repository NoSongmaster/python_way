#liuhao
#python2
# msg="中国"
# msg.decode(encoding="utf-8")
# print(msg)

#python3中,python解释器是以unicode编码，程序文件存储的是utf-8.
#当utf-8格式程序执行时解释器从内存中运行时全部转换成unicode。
'''
python3.X 默认文件是 utf-8
解释器编码是unicode,文件加载到内存后会自动编码成unicode，同时，把字符转换为byte类型
byte=8bit
'''
msg="中国"
print(msg.encode("gbk"))
#输出：b'\xd6\xd0\xb9\xfa'

f=open("file",'r+')
#省略编码时，默认使用操作系统的默认编码gbk格式。
'''
a  :追加
r+ :追加和读。从文件开始追加，可以定长修改。直接在原文内容上写入数据，擦除现有数据
w+ :清空原文件内容，再写入新内容。
a+ :追加+读，从文件末尾追加
f.seek(10),代表移动10个字节，注意汉字占用3个字节。
f.read(6),代表读取6个字符。

rb :以二进制模式打开文件，不能声明encoding。读取显示的时候使用decode
wb :以二进制写入文件，必须写入bytes格式。使用write写入时候，可以指定encode编码集
f.fileno() 文件描述符，
f.truncate(100) 从头开始截断100个字符，只能从头截断
'''