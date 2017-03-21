#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao
# import hashlib
# md5=hashlib.md5()
#
# md5.update(b'abc')
# md5.update(b'abc')
# print(md5.hexdigest().upper())
# # #74F23AFC9205A671C6971C6E960FF53C
# # #74F23AFC9205A671C6971C6E960FF53C
# md5=hashlib.md5()
# md5.update(b'abcabc')
# print(md5.hexdigest().upper())
# import sys,time
# def speed( a, b):  # 传入a,b输出进度，需要在外部调用做循环
#     output = sys.stdout
#     if a < b:
#         c = a / b * 100
#         count = int(c)
#         str_count = ('#' * count).ljust(100,)
#         output.write('\r完成进度 >:[%s]%.0f%%' % (str_count,c))
#         output.flush()
#     elif a == b:
#         c = a / b * 100
#         count = int(c)
#         str_count = ('#' * count).ljust(100,)
#         output.write('\r完成进度 >:[%s]%.0f%%' % (str_count, c))
#         print()
#     else:
#         print('传送完毕')
#
# a=0
# while True:
#     speed(a,100)
#     a+=1
#     if a >100:break
a ='..'
print(a.isalnum())
print(a.isidentifier())
import sys,platform
if platform.system() =='Windows':
    print(11111111)