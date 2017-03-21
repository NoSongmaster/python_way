#liuhao
import os
os.getcwd() #获取当前目录
os.chdir()  #切换目录
os.curdir   #返回当前目录
os.pardir   #获取当前目录的父目录字符串名
os.makedirs("d1/d2/d3") #创建多级目录
#如果文件存在，会报错。加入下面参数就不报错了
os.makedirs("d1/d2/d3",exist_ok=True)
os.listdir('.') #列出指定目录的文件
os.stat('') #查看文件详细属性
os.sep  #输出操作系统特定的路径分割符
os.linesep  #输出当前平台使用的行终止符。
os.name     #输出字符串指示当前系统
import platform
print(platform.system())    #查看操作系统简写
#system 每次调用会打开一个终端去执行
os.system("df -h")  #输出，但不会保存。只会返回命令执行结果的状态
os.popen("df -h").read()    #可以拿到命令的执行结果。
os.environ  #获取系统环境变量
os.path.abspath(__file__)   #通过相对路径返回程序的绝对路径 __file__ 是文件的相对路径
os.path.dirname()   #返回上一级目录
os.path.exists("path")#如果path存在返回True，不存在返回False




