#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao
#远程执行命令server端
import socket,subprocess,struct
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
phone.bind(('127.0.0.1',8080))
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
            res=subprocess.Popen(cmd.decode('utf-8'),   #通过subprocess获取命令的执行结果
                                        shell=True,
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE)
            err=res.stderr.read()   #获取错误信息
            if err: #如果错误信息存在
                back_msg=err    #返回信息为错误信息
            else:
                back_msg=res.stdout.read()  #否则返回信息为标准输出
        except Exception:       #
            break

        #解决服务端粘包问题
        conn.send(struct.pack('i',len(back_msg)))       #'i'：指定struct 返回的为4个字节
        conn.sendall(back_msg)                          #sendall 。循环将所有的数据全部发送完
    conn.close()    #挂电话
phone.close()   #关手机