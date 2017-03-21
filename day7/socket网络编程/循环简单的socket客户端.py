#liuhao
import socket
#客户端
#创建一个socket对象
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#利用socket对象进行连接server
client.connect(('127.0.0.1',8080))
while True:
    msg=input('>>:')
    if not msg:continue #如果输入的数据是空，返回
    client.send(msg.encode('utf-8'))    #进行发送数据,socket之间数据交互必须是bytes类型的
    data=client.recv(1024)              #进行接收数据
    print(data)
client.close()
