#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao
import socket,struct
#创建一个socket对象
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#进行连接服务器
client.connect(('127.0.0.1',8080))
#进入循环开始和服务器进行交互
while True:
    cmd=input('>>:').strip()
    if not cmd:continue #如果输入的是空，返回
    client.send(cmd.encode('utf-8'))
    data_head=client.recv(4)        #接收服务端用struct封装以后的数据,定长的为 4个字节
    data_size=struct.unpack('i',data_head)[0]   #利用struct获取到数据包的头部，获取到源数据的大小
    recv_size=0             #用来保存接收到的数据大小
    recv_bytes=b''          #用来保存接收到的数据
    while recv_size <data_size: #判断有没有收完数据
        res=client.recv(1024)   #接收数据
        recv_bytes+=res          #拼接bytes字符
        recv_size+=len(res)     #计算接收到的数据的大小
    print(res.decode('gbk'))    #打印接收到的数据
client.close()