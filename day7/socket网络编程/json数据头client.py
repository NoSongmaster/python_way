#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao
import socket,struct,json
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',8080))
while True:
    cmd=input('>>:').strip()
    if not cmd:continue
    client.send(cmd.encode('utf-8'))
    #收报头的长度
    data_head=client.recv(4)
   # data_size=json.load(struct.unpack('i',data_head)[0])
    head_size=struct.unpack('i',data_head)[0]
    #收报头（根据报头长度）
    head_json=client.recv(head_size)
    head_dict=json.loads(head_json.decode('utf-8'))
    #获取真实数据长度
    data_size=head_dict['data_size']

    recv_size=0
    recv_bytes=b''
    while recv_size <data_size:
        res=client.recv(1024)
        recv_bytes+=res
        recv_size+=len(res)
    print(res.decode('gbk'))
client.close()