#liuhao
import socket
#socket服务端:
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #买手机
phone.bind(('127.0.0.1',8080))                  #插入手机卡
phone.listen(5)         #开机     等待连接的连接数(5)     半连接池
conn,addr=phone.accept()     #接电话   conn连接的线路  addr 对方ip
print('tcp的连接: ',conn)
print('客户端的地址:',addr)
data=conn.recv(1024)         #接收的大小 1024
print('from client msg: %s' %data)

conn.send(data.upper()) #发消息

conn.close()    #挂电话
phone.close()   #关手机
