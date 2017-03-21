#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao

import socket,subprocess,struct,json
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #买手机
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
phone.bind(('127.0.0.1',8080))                  #插入手机卡
phone.listen(5)         #开机     等待连接的连接数(5)     半连接池
while True: #链接循环
    print('等待连接....')
    conn,addr=phone.accept()     #接电话   conn连接的线路  addr 对方ip
    print('tcp的连接: ',conn)
    print('客户端的地址:',addr)
    while True: #通讯循环
        try:
            cmd=conn.recv(1024)         #接收的大小 1024        #不能收空，空默认为没有收到
            if not cmd:break           #解决客户端断开，一直打印空。
            print('from client msg: %s' %cmd)
            res=subprocess.Popen(cmd.decode('utf-8'),
                                        shell=True,
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE)
            err=res.stderr.read()
            if err:
                back_msg=err
            else:
                back_msg=res.stdout.read()
        except Exception:       #
            break
        # conn.send(back_msg)
#解决服务端粘包问题
        #conn.send(struct.pack('i',json.dumps(len(back_msg))))
        #第一阶段，制作报头
        head_dict={
            'data_size':len(back_msg)
        }
        head_json=json.dumps(head_dict)
        head_bytes=head_json.encode('utf-8')
        #第二阶段：发送报头的长度
        conn.send(struct.pack('i',len(head_bytes)))
        #第三阶段：发送报头
        conn.send(head_bytes)
        #第四阶段：发送真实数据
        conn.sendall(back_msg)
    conn.close()    #挂电话
phone.close()   #关手机