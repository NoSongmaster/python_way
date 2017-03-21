# #liuhao
# '''文件拷贝，复制'''
import shutil
# f=open('123.bill')
# f2=open('123.bill_copy','w')
# shutil.copyfileobj(f,f2)  #传入文件对象
# #拷贝文件
# shutil.copyfile('123.bill','123.new')
# #仅拷贝文件属性
# shutil.copymode()
# #仅拷贝文件状态信息
# shutil.copystat()
# #拷贝文件和权限
# shutil.copy()
# #递归拷贝文件 利用ignore=() 过滤文件ignore=(shutil.ignore_patterns('*.log'))
# shutil.copytree(ignore=(shutil.ignore_patterns('*.log')))
# #递归删除文件，目录,没有排除
# shutil.rmtree()
# #创建压缩包，并返回文件路径
# shutil.make_archive("压缩名day5",'zip','被压缩文件绝对路径')

import zipfile
#压缩文件，压缩包名
# f=zipfile.ZipFile('ziptest.zip','w')
#压缩文件，指定文件路径,并去掉绝对路径，后改名
# f.write('C:\\Users\liuhao\PycharmProjects\s16\day6\\123.bill',arcname='123.bill')
# f.write('C:\\Users\liuhao\PycharmProjects\s16\day6\\123.bill',arcname='1.bill')
# f.write('C:\\Users\liuhao\PycharmProjects\s16\day6\\123.bill',arcname='12.bill')
# f.close()
#解压文件
# f=zipfile.ZipFile('ziptest.zip','r')
# #解压到当前路径
# # f.extract('123.bill')
# #全部解压，到指定路径
# #f.extractall(path='C:\\Users\liuhao\PycharmProjects\s16\day6')
# #解压到指定路径，指定文件
# f.extractall(path='C:\\Users\liuhao\PycharmProjects\s16\day6',members=['1.bill','12.bill'])