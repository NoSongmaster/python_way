#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao
# IO多路复用：8002,8001
#
import socket,select
sk1 = socket.socket()
sk1.bind(('127.0.0.1',8001,))
sk1.listen(5)

sk2 = socket.socket()
sk2.bind(('127.0.0.1',8002,))
sk2.listen(5)
inputs = [sk1,sk2,]
while True:
    # IO多路复用,同时监听多个socket对象
    #    - select,内部进行循环操作(1024)  主动查看
    #    - poll, 内部进行循环操作         主动查看
    #    - epoll,                        被动告知
    r,w,e = select.select(inputs,[],[],0.05)
    # r = [sk2,]        #r中只有请求来的时候才会有值，没有请求过来-就没有值
    # r = [sk1,]
    # r = [sk1,sk2]
    # r = []
    # r = [conn,]
    # r = [sk1,Wconn]
    #######？
    for obj in r:
        if obj in [sk1,sk2]:
            # 新连接捡来了...
            print('新连接来了:',obj)
            conn,addr = obj.accept()
            inputs.append(conn)     #将conn连接加入到进行监听的列表中
        else:
            # 有连接用户发送消息来了..
            print('有用户发送数据了:',obj)
            data = obj.recv(1024)
            obj.sendall(data)