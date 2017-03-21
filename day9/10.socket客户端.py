#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao
#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao
import socket

client = socket.socket()
client.connect(('127.0.0.1',8002,))

while True:
    v = input('>>>')
    client.sendall(bytes(v,encoding='utf-8'))
    ret = client.recv(1024)
    print('服务器返回：',ret)