#liuhao

print("from module sam")
mon=100
def read():
    print(mon)

print(__name__)
#把文件当做脚本执行__name__ 等于__main__
#把文件spam.py当做模块去使用__name__等于'spam'

if __name__ =='__main__':#应用场景：写入测试代码
    print("当文件当做脚本执行时，触发的代码")