#liuhao
#liuhao
import socket
#创建socket对象，指定家族簇，指定协议TCP=SOCK_STREAM
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#设置断开连接时不出错
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#绑定ip和port，注意传入一个参数元组类型
phone.bind(('127.0.0.1',8080))
phone.listen(5)         #开机     等待连接的连接数(5)     半连接池
while True: #链接循环
    conn,addr=phone.accept()     #conn是client连接成功创建的对象,之后的数据交互都是通过conn
    print('tcp的连接: ',conn)
    print('客户端的地址:',addr)
    while True: #通讯循环
        try:
            data=conn.recv(1024)         #接收的大小 1024        #不能收空，空默认为没有收到
            if not data:break           #解决客户端断开，一直打印空。
            print('from client msg: %s' %data)
            conn.send(data.upper()) #发消息    将client传入的数据转化为大写发送回去
        except Exception:       #
            break
    conn.close()    #挂电话
phone.close()   #关手机
