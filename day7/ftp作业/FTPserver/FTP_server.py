#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao
import socketserver,json,struct,os,sys,hashlib,subprocess,socket
class FTPServer(socketserver.BaseRequestHandler):
    def handle(self):
        self.base_dir=os.path.dirname(os.path.abspath(sys.argv[0]))

        print('连接socket信息: ',self.request)
        print('连接来自于: ',self.client_address)
        while True:
            try:
                if self.auth()['status'] is False:continue
            except Exception:break
            while True:
                try:
                    head_dict=self.recv_head()
                    if hasattr(self,head_dict['cmd']):
                        func=getattr(self,head_dict['cmd'])
                        func(head_dict)
                except Exception:
                    break
    def auth(self): #验证用户登录
        md5=hashlib.md5()
        head_dict=self.recv_head()  #这里只会接收到用户名和密码
        self.user_database = os.path.dirname(os.path.abspath(sys.argv[0])) + '/users' + '/' + head_dict['name'] #获得用户数据信息
        if os.path.isfile(self.user_database):
            with open(self.user_database,'r') as f:
                user_dict=json.load(f)
            if head_dict['name']==user_dict['name'] and head_dict['passwd']==user_dict['passwd']:
                head_dict=user_dict
                head_dict['status']=True
                self.send_head(head_dict)   #返回用户登录信息
                self.user_dir = os.path.dirname(os.path.abspath(sys.argv[0])) + '/user_file' + '/' + head_dict['name']  #ftp用户家目录
                self.root_dir = self.user_dir  # root_dict 用户临时目录集合
                return head_dict
        head_dict['status']=False
        self.send_head(head_dict)       #返回用户登录失败信息
        return head_dict
    def recv_head(self):    #接收client传来的报头
        data=self.request.recv(4)
        head_len = struct.unpack('i',data)[0]
        #print(head_len)
        head_bytes = self.request.recv(head_len)
        head_json = head_bytes.decode('utf-8')
        head_dict = json.loads(head_json)
        print('接收:',head_dict)
        return head_dict
    def send_head(self, head_dict):#向服务端发送 报头
        head_json = json.dumps(head_dict)
        head_bytes = head_json.encode('utf-8')
        print('发送:',head_dict)
        self.request.send(struct.pack('i', len(head_bytes)))
        self.request.send(head_bytes)
    def put(self,head_dict):#save 来自客户端的文件
        md5=hashlib.md5()
        self.user_files = os.path.dirname(os.path.abspath(sys.argv[0])) + '/user_file' + '/' + head_dict['name']+'/'+head_dict['file_name']
        file_path = self.user_files
        data_size = head_dict['file_size']
        print('in the server put')
        recv_size=0
        print(file_path)
        with open(file_path,'wb') as f:
            while True:
                if recv_size <data_size:
                    res=self.request.recv(1024)
                    f.write(res)
                    recv_size+=len(res)
                else:break
        with open(file_path,'rb') as f: #获取md5值
            for i in f:
                md5.update(i)
        if head_dict['md5_key'] ==md5.hexdigest():
            print('md5验证一致性：通过')
            self.send_head(head_dict)
        else:
            print('md5验证一致性：未通过')
            head_dict.pop('md5_key')
            self.send_head(head_dict)
       # print(md5.hexdigest())

    def get(self,head_dict):  #推送消息到
        md5=hashlib.md5()
        file_path=self.user_dir+'/'+head_dict['file_name']
        if os.path.exists(file_path) and os.path.isfile(file_path):
            file_name=os.path.basename(file_path)
            file_size=os.path.getsize(file_path)
            #print('in the server_get:',head_dict)
            with open(file_path,'rb') as f: #获取本地md5_key
                for i in f:
                    md5.update(i)
            head_dict['file_size']=file_size
            head_dict['md5_key']=md5.hexdigest()
            head_dict['get_status']=True
            #print(head_dict)
            self.send_head(head_dict)
            with open(file_path,'rb') as f:
                for line in f:
                    self.request.send(line)


    def cmd(self,head_dict):
        msg='false'
        #self.user_dir = os.path.dirname(os.path.abspath(sys.argv[0])) + '/user_file' + '/' + head_dict['name']
        #print(head_dict)
        cmd_list=head_dict['cmd_str'].split()

        print(cmd_list)
        #cmd_list = ['ls', 'mkdir', 'cd','dir']
        if len(cmd_list)==1 and cmd_list[0] in ['ls','dir','pwd']:
            if cmd_list[0]=='pwd':
                msg=self.root_dir
            elif cmd_list[0]=='dir':
                os.chdir(self.root_dir)
                cmd_str='dir'
            else: cmd_str=cmd_list[0]+' '+self.root_dir

        elif len(cmd_list)==2 :

            if cmd_list[0] in ['mkdir','cd']:
                #isidentifier 合法的标识符   isalnum 数字或字符
                if cmd_list[1].isidentifier() or cmd_list[1].isalnum():
                    cmd_str=cmd_list[0]+' '+self.root_dir+'/'+cmd_list[1]
                    if cmd_list[0]=='cd' and os.path.isdir(self.root_dir+'/'+cmd_list[1]):
                        self.root_dir+='/'+cmd_list[1]
                elif cmd_list[0]=='cd' and cmd_list[1]=='..':       #返回上一级目录
                    self.root_dir=os.path.dirname(self.root_dir)
                    if self.root_dir in self.user_dir:      #判断上级目录是不是家目录
                        self.root_dir=self.user_dir
                    cmd_str=head_dict['cmd_str']
            elif head_dict['cmd_str'] =='ls -l':
                cmd_str=head_dict['cmd_str']
        print('消息:',msg)
        if msg =='false':
            res = subprocess.Popen(cmd_str,
                                   shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            err=res.stderr.read()
            if err:
                msg=err
            else:msg=res.stdout.read()

            self.request.send(struct.pack('i',len(msg)))
            self.request.sendall(msg)
        else:
            self.request.send(struct.pack('i',len(msg)))
            self.request.sendall(msg.encode('gbk'))

if __name__ == '__main__':
    s=socketserver.ThreadingTCPServer(('127.0.0.1',8080),FTPServer)
    s.socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.serve_forever()