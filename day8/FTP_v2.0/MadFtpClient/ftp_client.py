import socket
import os ,json
import optparse
import getpass
import hashlib
import sys
import struct

STATUS_CODE  = {        #定义status的状态码
    250 : "Invalid cmd format, e.g: {'action':'get','filename':'test.py','size':344}",
    251 : "Invalid cmd ",
    252 : "Invalid auth data",
    253 : "Wrong username or password",
    254 : "Passed authentication",
}



class FTPClient(object):
    def __init__(self):
        self.user = None        #记录登录的用户
        parser = optparse.OptionParser()        #自定义命令行的参数
        parser.add_option("-s","--server", dest="server", help="ftp server ip_addr")
        parser.add_option("-P","--port",type="int", dest="port", help="ftp server port")
        parser.add_option("-u","--username", dest="username", help="username")
        parser.add_option("-p","--password", dest="password", help="password")
        self.options , self.args = parser.parse_args()
        self.verify_args(self.options,self.args)
        self.make_connection()

    def make_connection(self):  #创建连接
        self.sock = socket.socket()
        self.sock.connect((self.options.server,self.options.port))  #根据命令行提供的参数连接 ip 和 port

    def verify_args(self, options,args):
        '''校验参数合法型'''

        if options.username is not None and options.password is not None:   #不论有没有传入用户名和密码都通过
            pass
        elif options.username is None and options.password is None:
            pass
        else:
            #options.username is None or options.password is None:
            exit("Err: username and password must be provided together..")

        if options.server and options.port:     #校验端口 0-65535
            #print(options)
            if options.port >0 and options.port <65535:
                return True #返回true
            else:
                exit("Err:host port must in 0-65535")
        else:
            exit("Error:must supply ftp server address, use -h to check all available arguments.")

    def authenticate(self):
        '''用户验证'''
        if self.options.username:   #如果命令行出入了用户名
            print(self.options.username,self.options.password)  #打印传入的用户名和密码
            return  self.get_auth_result(self.options.username, self.options.password)  #验证用户名密码  返回验证状态
        else:   #如果命令行的时候没有输入用户名和密码
            retry_count = 0
            while retry_count <3:       #可以进行三次验证
                username = input("username:").strip()
                password = input("password:").strip()
                if self.get_auth_result(username,password): #验证用户名和密码： 如果通过验证
                    return True         #返回验证为True
                retry_count += 1



    def get_auth_result(self,user,password):    #输入用户名和密码
        md5=hashlib.md5()
        md5.update(password.encode())        #使用加密验证用户密码
        print(md5.hexdigest())
        data = {'action':'auth',        #定义一个字典进行验证，这里是执行的动作:验证
                'username':user,
                'password':md5.hexdigest()}     #发送的时候是加密以后的密码，安全性提高
        self.sock.send(json.dumps(data).encode())   #发送字典到server
        #self.sock.recv(1024)
        response = self.get_response()              #获取server返回的信息，一个字典格式

        if response.get('status_code') == 254:  #如果server返回的status_code 是254 说明验证成功
            print("Passed authentication!")
            self.user = user                        #定义self.user=user
            return True                             #返回验证信息true
        else:
            print(response.get("status_msg"))         #其它的打印server返回值

    def get_response(self):
        '''得到服务器端回复结果'''
        data = self.sock.recv(1024)     #获取数据
        #print("server res", data)
        data = json.loads(data.decode())    #json加载server返回的字典
        return data                 #返回这个字典



    def interactive(self):          #server 和client 交互的程序
        if self.authenticate(): #如果进行验证，通过：
            print("---start interactive with u...")
            self.terminal_display = "[%s]$:"%self.user      #self.teminal_display        #####[alex]:
            while True:
                choice = input(self.terminal_display).strip()   #用户输入操作命令
                if len(choice) == 0:continue
                cmd_list = choice.split()   #切割命令
                if hasattr(self,"_%s"%cmd_list[0]): #判断指令是否在这个类中存在
                    func = getattr(self,"_%s"%cmd_list[0])  #如果存在，获取这个方法
                    func(cmd_list)  #执行这个方法
                else:
                    print("Invalid cmd,type 'help' to check available commands. ")
    
    def __md5_required(self,cmd_list):
        '''检测命令是否需要进行MD5验证'''
        if '--md5' in cmd_list: #判断这个命令中是否 加入 --md5 如果加入了 返回true
            return True


    def _help(self,*args,**kwargs): #如果键入的命令是help
        supported_actions = """
        get filename    #get file from FTP server
        put filename    #upload file to FTP server
        ls              #list files in current dir on FTP server
        pwd             #check current path on server
        cd path         #change directory , same usage as linux cd command
        """
        print(supported_actions)

    def show_progress(self,total):  #打印进度条，生成器
        received_size = 0       #已经接收的字节大小
        current_percent = 0     #正在接受的百分比
        while received_size < total:    #如果已经接受字节的大小小于总字节的大小
             if int((received_size / total) * 100 )   > current_percent :   #如果接收的进度大于  已经接受的百分比
                  print("#",end="",flush=True)  #打印一个#
                  current_percent = int((received_size / total) * 100 ) #计算正在接受的 进度百分比
             new_size = yield               #生成器， 传入一个新的大小
             received_size += new_size          #已经接受的大小

    def _cd(self,*args,**kwargs):#cd 命令
        #print("cd args",args)
        if len(args[0]) >1:     #如果传入的是两个以上的参数
            path = args[0][1]   #path = 后面传入的参数
        else:
            path = ''            #否则 path= ' '
        data = {'action': 'change_dir','path':path} #发送字典 动作:change_dir   path=path
        self.sock.send(json.dumps(data).encode())   #发送到server端
        response = self.get_response()              #接收server的返回值
        if response.get("status_code") == 260: #如果 返回值status_code =260
            #将显示的teminal_display=相对的路径，显示的路径发生了改变
            self.terminal_display ="%s:" % response.get('data').get("current_path")
            #
    def speed(self,total):  # 传入a,b输出进度，需要在外部调用做循环
        output = sys.stdout
        received_size=0
        current_percent =0
        while received_size <= total:
            if (int( received_size / total * 100))>current_percent:
                current_percent = int((received_size / total) * 100)
                str_count = ('#' * current_percent).ljust(100, )
                output.write('\r完成进度 >:[%s]%.0f%%' % (str_count, current_percent))
                output.flush()
                if current_percent==100:
                    print()

            new_size=yield
            received_size+=new_size

    def _pwd(self,*args,**kwargs):  #pwd 命令   #这个命令不需要传入参数，
        data = {'action':'pwd'}     #封装一个字典
        self.sock.send(json.dumps(data).encode())   #将这个字典发送到server
        response = self.get_response()              #获取到server的返回值
        has_err = False                             #先定义 has_err
        if response.get("status_code") == 200:  #如果返回值是200
            data = response.get("data") #data=服务端返回的data

            if data:        #如果data不为空 打印 data
                print(data)
            else:
                has_err = True  #其它设置has_err
        else:   #如果返回值不是200 .设置 has_err
            has_err = True

        if has_err: #如果有错误， 打印
            print("Error:something wrong.")

    def _ls(self,*args,**kwargs):
        data = {'action':'listdir'}     #动作:listdir
        self.sock.send(json.dumps(data).encode())       #发送定义好的字典
        response = self.get_response()  #获取server端的字典
        has_err = False
        if response.get("status_code") == 200:  #如果server的返回status_code=200
            data = response.get("data") #data=server[data]

            if data:    #如果返回的data不为空
                print(data[1])  #打印data[1]   注:subprocess.getstatusoutput(cmd) 获取(状态,命令返回结果)
            else:
                has_err = True
        else:
            has_err = True

        if has_err:
            print("Error:something wrong.")
    def _put(self,cmd_list):
        print('put---',cmd_list)
        if len(cmd_list)==1:
            print("no filename follows...")
            return

        data_header = {  # 定义字典
            'action': 'put',  # 动作:put
        }
        file_path=cmd_list[1]
        if self.__md5_required(cmd_list):
            data_header['md5']=True
        else:data_header['md5']=False
        if os.path.isfile(file_path):
            print('os.path.isfile:216')
            filename=os.path.basename(cmd_list[1])
            data_header['filename']=filename
            data_header['file_size']=os.path.getsize(file_path)
        else:return
        self.sock.send(json.dumps(data_header).encode())  # 发送字典
        print(data_header)
        if self.__duandian(cmd_list): return

        self.sock.recv(1)   #接收到确认信息，可以开始发送数据
        file_obj=open(file_path,'rb')
        if data_header.get('md5'):
            md5_obj=hashlib.md5()
            progress = self.speed(data_header['file_size'])  # generator
            progress.__next__()
            for i in file_obj:
                self.sock.send(i)
                md5_obj.update(i)
                try:
                    progress.send(len(i))
                except StopIteration as e:
                    print()
            else:
                print('上传数据完成')
                self.sock.recv(1)   #等待对方确认
                file_obj.close()
                md5_val=md5_obj.hexdigest()
                print(md5_val)
                md5_from_server=self.get_response()
                if md5_from_server['status_code'] == 258:
                    if md5_from_server['data'] == md5_val:  # 进行对比server端和本地的md5
                        print("%s 文件一致性校验成功!" % file_path)
        else:
            progress = self.speed(data_header['file_size'])  # generator
            progress.__next__()
            for i in file_obj:
                self.sock.send(i)
                try:
                    progress.send(len(i))
                except StopIteration as e:
                    print()
            else:
                self.sock.recv(1)  # 等待对方确认
                file_obj.close()
    def recv_head(self):    #接收client传来的报头
        data=self.sock.recv(4)
        head_len = struct.unpack('i',data)[0]
        #print(head_len)
        head_bytes = self.sock.recv(head_len)
        head_json = head_bytes.decode('utf-8')
        head_dict = json.loads(head_json)
        print('接收:',head_dict)
        return head_dict
    def send_head(self, head_dict):#向服务端发送 报头
        head_json = json.dumps(head_dict)
        head_bytes = head_json.encode('utf-8')
        print('发送:',head_dict)
        self.sock.send(struct.pack('i', len(head_bytes)))
        self.sock.send(head_bytes)
    def __duandian(self,cmd_list):
        print('--断点续传-校验')
        data_header = {  # 定义字典
            'action': 'put',  # 动作:put
        }
        file_path = cmd_list[1]
        if os.path.isfile(file_path):

            filename=os.path.basename(cmd_list[1])
            data_header['filename']=filename
            data_header['file_size']=os.path.getsize(file_path)
        else:return
        self.send_head(data_header)
        dd_dict=self.recv_head()
        print(dd_dict)
        if dd_dict.get('dd'):
            print('文件断点，确认存在')
            file_obj=open(file_path,'rb')
            file_obj.seek(dd_dict.get('ddfile_size'))
            print('开始断点续传')
            progress = self.speed(data_header['file_size'])  # generator
            progress.__next__()
            progress.send(dd_dict.get('ddfile_size'))
            for line in file_obj:
                self.sock.send(line)
                try:
                    progress.send(len(line))
                except StopIteration as e:
                    print()
            file_obj.close()
            md5_res=self.recv_head()
            server_md5=md5_res.get('md5')
            file=open(file_path,'rb')
            md5_client=hashlib.md5()
            for i in file:
                md5_client.update(i)
            client_md5_val=md5_client.hexdigest()
            if client_md5_val==server_md5:
                print('一致性校验通过')
            else:print('断点续传有问题')
            return True
        else:return False


    def _get(self,cmd_list):
        print("get--",cmd_list)
        if len(cmd_list) == 1:
            print("no filename follows...")
            return
        data_header = {     #定义字典
            'action':'get',         #动作:get
            'filename':cmd_list[1]
        }
        if self.__md5_required(cmd_list):   #验证是否存在 --md5
            data_header['md5'] = True       #在字典中加入 md5=true

        self.sock.send(json.dumps(data_header).encode())    #发送字典
        response = self.get_response()      #获取server端的返回值
        print(response)
        if response["status_code"] == 257:#ready to receive     #如果 返回值status_code =257
            self.sock.send(b'1')#send confirmation to server    #发送1个字典的内容。解决粘包问题
            base_filename = cmd_list[1].split('/')[-1]      #用/进行切割，获取最后面一个真实的文件名称
            received_size = 0                               #已经接受的文件大小
            file_obj = open(base_filename,"wb")            #打开一个文件
            if response['data']['file_size'] == 0:      #如果获取到的file_size=0 关闭文件，本地创建了一个新的文件
                file_obj.close()
                return

            if self.__md5_required(cmd_list):       #如果有--md5校验
                md5_obj = hashlib.md5()              #创建一个md5校验的实例
                progress = self.speed(response['data']['file_size']) #generator     #使用生成器，传入文件总大小
                progress.__next__() #调用生成器__next__()
                while received_size < response['data']['file_size']:    #如果已经接受的大小,小于总大小
                    data = self.sock.recv(4096)                            #开始接受数据
                    received_size += len(data)                              #已经接收得长度
                    try:
                      progress.send(len(data))                               #将新接收的数据的长度 send 发送给生成器调用|开始走到__next__()。在往下走
                    except StopIteration as e:      #如果全部走完了会报错
                      print()
                    file_obj.write(data)        #写入每一次接收的数据
                    md5_obj.update(data)        #校验每一次接收的数据
                else:#如果接收完毕的话，
                    self.sock.send(b'1')   #确认接收完数据，解决粘包
                    print("----->file recv done----")
                    file_obj.close()    #关闭文件
                    md5_val = md5_obj.hexdigest()   #生成文件的md5校验码
                    md5_from_server = self.get_response()       #从服务端获取md5校验码
                    if md5_from_server['status_code'] == 258:   #如果服务端返回的状态码是258 .
                        print(md5_val)
                        print(md5_from_server)
                        if md5_from_server['data'] == md5_val:       #进行对比server端和本地的md5
                            print("%s 文件一致性校验成功!" % base_filename)
                    #print(md5_val,md5_from_server)

            else:       #如果不进行md5校验，
                progress = self.speed(response['data']['file_size']) #generator
                progress.__next__()

                while received_size < response['data']['file_size']:    #进行数据接收
                    data = self.sock.recv(4096)                     #
                    received_size += len(data)
                    file_obj.write(data)                            #将接收的数据写入文件
                    try:
                      progress.send(len(data))                       #调用生成器。打印进度条
                    except StopIteration as e:
                      print()                             #抛出异常，打印输出100%

                else:
                    # self.sock.send(b'1')  # 确认接收完数据，解决粘包
                    print("----->file rece done----")
                    file_obj.close()

if __name__ == "__main__":
    ftp = FTPClient()
    ftp.interactive() #交互
