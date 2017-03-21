#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao
from socket import *
from time import sleep
import os,json,struct,hashlib,sys,random
import time
class FTPClient():
    def __init__(self,ip,port,AF_INET=AF_INET,SOCK_STREAM=SOCK_STREAM):

        self.client=socket(AF_INET,SOCK_STREAM)
        self.client.connect((ip,port))
    def login(self):
        while True:
            md5_passwd = hashlib.md5()
            name=input('enter your name:').strip()
            if len(name)==0:continue
            passwd=input('enter your passwd:')
            if len(passwd)==0:continue
            md5_passwd.update(passwd.encode(encoding='utf-8'))
            login_dict={'name':name,
                        'passwd':md5_passwd.hexdigest()
                        }
            self.send_head(login_dict)
            head_dict=self.recv_head()
            if head_dict['status']:
                print('验证通过')
                return head_dict
            else:
                print('验证失败')
                return head_dict
    def recv_head(self):
        data = self.client.recv(4)
        head_len = struct.unpack('i',data)[0]
        head_bytes = self.client.recv(head_len)
        head_json = head_bytes.decode('utf-8')
        head_dict = json.loads(head_json)
        #print('接收',head_dict)
        return head_dict
    def run(self,user_dict):
        while True:
            cmd_list = ['ls', 'mkdir', 'cd','dir','pwd']
            cmd_str=input('enter your action: ').strip()
            if not cmd_str:continue
            if len(cmd_str.split(' '))==2:
                cmd,file_path=cmd_str.split()
                if hasattr(self,cmd):            #判断get,put
                    func=getattr(self,cmd)
                    func(file_path,user_dict)
                if cmd in cmd_list:              # 判断cmd
                    cmd='cmd'
                    if hasattr(self, cmd):
                        func = getattr(self, cmd)
                        func(cmd_str,user_dict)
            elif len(cmd_str.split(' '))==1:
                if cmd_str.split()[0] in ['mkdir','cd']:continue
                if cmd_str.split()[0] in cmd_list:
                    cmd = 'cmd'
                    if hasattr(self, cmd):
                        func = getattr(self, cmd)
                        func(cmd_str, user_dict)
            else:continue
    def send_head(self,head_dict):
        #print('发送',head_dict)
        head_json = json.dumps(head_dict)
        head_bytes = head_json.encode('utf-8')
        self.client.send(struct.pack('i', len(head_bytes)))
        self.client.sendall(head_bytes)

    def speed(self,a, b,seed):  # 传入a,b输出进度，需要在外部调用做循环
        output = sys.stdout
        if a < b:

            c = a / b * 100
            count = int(c)
            str_count = ('#' * count).ljust(100, )
            output.write('\r完成进度 >:[%s]%.0f%%  %s' % (str_count, c,seed))
            output.flush()
        elif a == b:
            c = a / b * 100
            count = int(c)
            str_count = ('#' * count).ljust(100, )
            output.write('\r完成进度 >:[%s]%.0f%%' % (str_count, c))
            print()
        else:
            print('传送完毕')
    def put(self,file_path,user_dict):
        self.md5 = hashlib.md5()
        if os.path.exists(file_path) and os.path.isfile(file_path):
            file_name=os.path.basename(file_path)
            file_size=os.path.getsize(file_path)
            with open(file_path,'rb') as f:
                for i in f:
                    self.md5.update(i)
            #封装头部字典,json保存字典,
            user_dict['cmd']='put'
            user_dict['file_name']=file_name
            user_dict['file_size']=file_size
            user_dict['md5_key']=self.md5.hexdigest()
           # print(user_dict)
            self.send_head(user_dict)
            lang=0
            with open(file_path,'rb') as f:
                for line in f:
                    lang+=len(line)
                    if file_size >10000000:    #当文件大于10M时
                        for i in range(2):
                            current = random.randrange(0,100)
                            if i ==current:
                                self.speed(lang, user_dict['file_size'])
                    else:
                        self.speed(lang, user_dict['file_size'])
                    self.client.sendall(line)
                    #if lang==user_dict['file_size']:self.speed(lang, user_dict['file_size'])
            print()
            md5_dict=self.recv_head()
            if 'md5_key' in md5_dict:
                print('md5验证：通过')
            else:print('md5验证：未通过')
    def get(self,file_name,user_dict):
        md5=hashlib.md5()
        #print(file_name,user_dict)
        user_dict['cmd']='get'
        user_dict['file_name']=file_name
        self.send_head(user_dict)
        get_dict=self.recv_head()
       # print('get_dict',get_dict)
        if get_dict['get_status']:
            file_size=get_dict['file_size']
            recv_size=0
            sped=0
            with open(get_dict['file_name'],'wb') as f: #接收文件,并打印进度条
                while True:
                    if recv_size< file_size:
                        if file_size > 10000000:  # 当文件大于10M时

                            for i in range(2):  #取随机数，输出进度条
                                current = random.randrange(0,100)
                                if i == current:
                                    self.speed(recv_size, get_dict['file_size'],sped)
                        else:
                            self.speed(recv_size, get_dict['file_size'],sped)
                        time_start = time.time()
                        recv_data=self.client.recv(1024)

                        print(time_start)
                        time.sleep(1)
                        # sped=len(recv_data)/(time_stop-time_start)
                        f.write(recv_data)
                        recv_size += len(recv_data)
                        md5.update(recv_data)
                    else:break
                #print(md5.hexdigest())
            print()
            if get_dict['md5_key']==md5.hexdigest():
                print('MD5一致性验证：通过')
            else:print('MD5一致性验证：未通过')
    def cmd(self,cmd_str,user_dict):
        print(cmd_str)
        user_dict['cmd']='cmd'
        user_dict['cmd_str']=cmd_str
        self.send_head(user_dict)
        head=self.client.recv(4)
        data_size = struct.unpack('i', head)[0]
        recv_size = 0  # 用来保存接收到的数据大小
        recv_bytes = b''  # 用来保存接收到的数据
        while recv_size < data_size:  # 判断有没有收完数据
            res = self.client.recv(1024)  # 接收数据
            recv_bytes += res  # 拼接bytes字符
            recv_size += len(res)  # 计算接收到的数据的大小
        print(recv_bytes.decode('gbk'))  # 打印接收到的数据
def run_main():
    while True:
        try:
            ip = input('enter ftp server_IP port:').strip()
            ip_port = ip.split()
            if len(ip_port) == 2:
                a = FTPClient(ip_port[0], int(ip_port[1]))  # 正式使用

                user_dict = a.login()
                if user_dict['status']:
                    a.run(user_dict)
                else:
                    print('请重新登陆')
            else:
                continue
        except Exception:
            continue

def test_main():
    # a = FTPClient('172.16.50.91',8080)  #测试
    a = FTPClient('127.0.0.1', 8080)  # 测试
    user_dict = a.login()
    if user_dict['status']:
        a.run(user_dict)
    else:
        print('请重新登陆')




if __name__ == '__main__':
    #run_main()         #正式使用
    test_main()         #测试使用
'''
c=socket(AF_INET,SOCK_STREAM)
c.connect(('127.0.0.1',8080))
'''





