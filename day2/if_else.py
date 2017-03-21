#liuhao
#if else简单应用
#场景一、用户登录验证
import getpass
name = input("请输入用户名：")
pwd= input("请输入密码")
#使用getpass模块隐藏用户输入密码，但是pycharm不支持~
#pwd=getpass.getpass("请输入用户名")
if name=='alex' and pwd=='123':
    print("验证通过")
else:
    print("验证失败")





