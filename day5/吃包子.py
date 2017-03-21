#liuhao
'''
通过yield实现在单线程的情况下实现并发运算的效果
'''
import time
# def consumer(name):
#     print("%s 准备吃包子啦!" %name)
#     while True:
#        #yield 接收producer， send过来的参数,赋值给baozi变量
#        baozi = yield
#
#        print("包子[%s]来了,被[%s]吃了!" %(baozi,name))
#
# def producer(name):
#     c = consumer('A')
#     c2 = consumer('B')
#     c.__next__()
#     c2.__next__()
#     print("老子开始准备做包子啦!")
#     for i in range(10):
#         time.sleep(1)
#         print("做了2个包子!")
#         #send 是唤醒生成器，并传参给yeild ，next只能唤醒不能传参
#         c.send(i)
#         c2.send(i)
#
# producer("alex")

def xiaofeizhe(name):
    print("%s准备吃包子"%name)
    while True:
        baozi=yield
        print("来了第%s个包子, 被%s吃了"%(baozi,name))

def chushi(name):
    print("%s 开始做饭了"%name)
    x1=xiaofeizhe("贺磊")
    x2=xiaofeizhe("磊磊")
    x1.__next__()
    x2.__next__()
    for i in range(10):
        print("第%s个包子来了"%i)
        time.sleep(1)
        x1.send(i)
        x2.send(i)
chushi("浩哥")

