import socketserver
import configparser
from conf import settings
import os,subprocess
import hashlib
import re
import struct

STATUS_CODE  = {
    200 : "Task finished",
    250 : "Invalid cmd format, e.g: {'action':'get','filename':'test.py','size':344}",
    251 : "Invalid cmd ",
    252 : "Invalid auth data",
    253 : "Wrong username or password",
    254 : "Passed authentication",
    255 : "Filename doesn't provided",
    256 : "File doesn't exist on server",
    257 : "ready to send file",
    258 : "md5 verification",
    259 : "path doesn't exist on server",
    260 : "path changed",
}

import json
class FTPHandler(socketserver.BaseRequestHandler):

    def handle(self):       #用于与客户端交互
        while True:
            self.data = self.request.recv(1024).strip() #接收数据
            print(self.client_address[0])   #打印客户端的信息
            print(self.data)                #打印接收的字典
            if not self.data:               #如果接收到空数据包
                print("client closed...")   #打印client 连接关闭
                break                   #跳出循环

            data  = json.loads(self.data.decode())    #json加载获取的字典


            if data.get('action') is not None:  #如果字典中传入了action---key
                #print("---->",hasattr(self,"_auth"))
                if hasattr(self,"_%s"%data.get('action')): #_auth       #判断传入的action是否存在
                    func = getattr(self,"_%s"% data.get('action'))  #如果存在，进行调用
                    func(data)
                else:       #server不存在这个方法
                    print("invalid cmd")
                    self.send_response(251)     #发送给客户端
            else:
                print("invalid cmd format") #如果接收到的action不存在
                self.send_response(250)         #发送格式错误

    def send_response(self,status_code,data=None):  #默认只发送status_code
        '''向客户端返回数据'''
        response = {'status_code':status_code,
                    'status_msg':STATUS_CODE[status_code],
                    }
        #print("data",data)
        if data:    #如果传入data
            #print("goes here....")
            response.update( { 'data': data  }) #在字典中加入data
        #print("-->data to client",response)
        self.request.send(json.dumps(response).encode())    #发送整个字典

    def _auth(self,*args,**kwargs):         #用户验证方法：
        data = args[0]          #客户端传入的数据
        if data.get("username") is None or data.get("password") is None:    #如果用户名和密码不存在
            self.send_response(252)         #发送数据，与客户端此次交互完成

        user = self.authenticate(data.get("username"),data.get("password")) #如果验证通过,返回的是用户名称
        if user is None: #failed auth   #如果用户不存在
            self.send_response(253)         #发sing错误的用户或密码，交互完成
        else:   #成功
            print("passed authentication",user)
            self.user = user    #将user设置成全局的【这个是个字典】
            self.user['username'] =  data.get("username")   #设置为客户端传来的用户名

            self.home_dir = "%s/home/%s" %(settings.BASE_DIR,data.get("username"))  #拼接用户的家目录
            self.current_dir = self.home_dir        #拼接用户所在的相对目录
            self.send_response(254) #发送验证通过
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

    def authenticate(self,username,password):
        '''验证用户合法性，合法就返回用户数据'''
        md5=hashlib.md5()
        config = configparser.ConfigParser()        #生成一个实例，config
        config.read(settings.ACCOUNT_FILE)          #利用实例读取sttings下的ACCOUNT_FILE
        if username in config.sections():           #如果用户名在这个配置实例的sections
            _password = config[username]["Password"]    #定义变量_password 获取配置文件中的用户密码
            md5.update(_password.encode())       #使用md5加密校验用户密码
            print(md5.hexdigest())
            if md5.hexdigest() == password:     #如果加密后的server上用户密码 和传来的密码相等
                print("pass auth..",username)       #打印验证通过
                config[username]["Username"] = username     #写入配置文件， Username= username
                return config[username]     #返回配置文件中的username

    def _put(self,*args,**kwargs):
        "client send file to server"
        pass

    def _listdir(self,*args,**kwargs):      #ls方法
        """return file list on current dir"""
        res = self.run_cmd("ls -lsh %s" %self.current_dir)

        self.send_response(200, data=res)       #发送200状态码，返回data元组

    def run_cmd(self,cmd):
        cmd_res = subprocess.getstatusoutput(cmd)       #利用subprocess 返回执行状态和执行结果
        return cmd_res

    def _change_dir(self, *args,**kwargs):
        """change dir"""
        #print( args,kwargs)
        if args[0]: #"" #传入的参数不为空：
            dest_path = "%s/%s" % (self.current_dir,args[0]['path'] )   #拼接用户的切换路径data[path] 就是目录名称
        else:
            dest_path = self.home_dir       #其它的切换路径还是家目录
        print("dest path",dest_path)

        real_path = os.path.realpath(dest_path)     #获取拼接后的  真实绝对路径
        print("readl path ", real_path)
        if real_path.startswith(self.home_dir):# accessable     #如果要切换的真实路径是以家目录开头的
            if os.path.isdir(real_path):    #并且这个路径存在
                self.current_dir = real_path        #将当前路径 修改为 要切换的路径
                current_relative_dir = self.get_relative_path(self.current_dir)     #当前路径的  相对路径/home/alex/....
                self.send_response(260, {'current_path':current_relative_dir})  #发送当前路径，为相对路径，封装了一个字典传入到data中
            else:
                self.send_response(259) #如果这个路径不存在，发送259 状态码
        else:   #如果要切换的路径不是以 家目录开头的
            print("has no permission....to access ",real_path)
            current_relative_dir = self.get_relative_path(self.current_dir) #相对路径=当前路径的相对路径
            self.send_response(260, {'current_path': current_relative_dir}) #发送相对路径到client

    def get_relative_path(self,abs_path):
        """return relative path of this user"""
        relative_path = re.sub("^%s"%settings.BASE_DIR, '', abs_path)   #从传入的绝对路径中，截取相对路径，去掉BASE_DIR部分
        # if not relative_path: #means the relative path equals to home dir
        #     relative_path = abs_path
        #
        print(("relative path",relative_path,abs_path))
        return relative_path    #返回相对路径


    def _pwd(self,*args,**kwargs):
        #res = self.run_cmd("pwd")
        current_relative_dir = self.get_relative_path(self.current_dir) #获取当前路径的相对路径----
        self.send_response(200,data=current_relative_dir)   #发送相对路径到对端

    def _get(self,*args,**kwargs):      #给client发送数据
        data = args[0]          #
        if data.get('filename') is None:    #如果获取到的文件名是空，
            self.send_response(255)
        #user_home_dir = "%s/%s" %(settings.USER_HOME,self.user["Username"])
        file_abs_path = "%s/%s" %(self.current_dir,data.get('filename'))    #获取文件的绝对路径
        print("file abs path",file_abs_path)        #打印文件的绝对路径

        if os.path.isfile(file_abs_path):   #如果是个文件
            file_obj = open(file_abs_path,"rb") #打开文件
            file_size = os.path.getsize(file_abs_path)  #获取文件的大小
            self.send_response(257,data={'file_size':file_size})    #发送字典，文件的大小
            self.request.recv(1) #等待客户端确认                   #解决粘包，等待确认

            if data.get('md5'):     #如果获取到的字典中包含 key为md5
                md5_obj = hashlib.md5()     #获取md5校验的实例
                for line in file_obj:   #读取文件的内容
                    self.request.send(line) #发送每一行读取的内容
                    md5_obj.update(line)    #进行md5校验
                else:
                    print(1111111111111)
                    self.request.recv(1)    #解决粘包，数据发送完成
                    file_obj.close()    #发送完成，关闭文件
                    md5_val = md5_obj.hexdigest()   #获取校验的md5 哈希值
                    print(md5_val)
                    self.send_response(258,data=md5_val)   #发送md5 校验值到客户端
                    print("send file done....")
            else:   #如果没有md5 校验
                for line in file_obj:   #读取文件
                    self.request.send(line) #发送每一行
                else:#读取完毕
                    # self.request.recv(1)
                    file_obj.close()    #关闭文件
                    print("send file done....")
        else:
            self.send_response(256) #如果不是文件，发送256状态码
    def _put(self,*args,**kwargs):

        data = args[0]  #
        print(data)
        if self.__duandian():return
        file_abs_path= "%s/%s" %(self.current_dir,data.get('filename'))
        print(file_abs_path)
        file_obj = open(file_abs_path, "wb")  # 打开文件
        file_size=data.get('file_size')
        #if self.__duandian(data): return
        self.request.send(b'1') #发送确认等待接收数据
        recv_size=0
        if data['md5']:
            md5_obj=hashlib.md5()
            while recv_size < file_size:
                data=self.request.recv(4096)
                recv_size+=len(data)
                file_obj.write(data)
                md5_obj.update(data)
            else:
                #print(recv_size)
                self.request.send(b'1')
                print('recv done------put')
                file_obj.close()
                md5_val=md5_obj.hexdigest()
                self.send_response(258,data=md5_val)
        else:
            while recv_size<file_size:
                data=self.request.recv(4096)
                recv_size+=len(data)
                file_obj.write(data)
            else:
                self.request.send(b'1')
                file_obj.close()

    def __duandian(self,*args,**kwargs):
        recv_dict=self.recv_head()
        md5_dd=hashlib.md5()
        file_abs_path = "%s/%s" % (self.current_dir, recv_dict.get('filename'))
        print(file_abs_path)
        print(os.path.exists(file_abs_path))
        if os.path.exists(file_abs_path):
            server_file_size = os.path.getsize(file_abs_path)
            if os.path.isfile(file_abs_path):
                print('server_size:',server_file_size)
                print('client_size:',recv_dict.get('file_size'))
                if server_file_size < recv_dict.get('file_size'):
                    file_obj = open(file_abs_path,'rb')
                    for i in file_obj:
                        md5_dd.update(i)
                    md5_val2=md5_dd.hexdigest()
                    res1_dict={'md5':md5_val2,
                               'ddfile_size':server_file_size,
                               'dd':True
                               }
                    print(res1_dict)
                    self.send_head(res1_dict)
                    file_obj.close()
                    file_append=open(file_abs_path,'ab+')
                    recv_size=server_file_size
                    while recv_size < recv_dict.get('file_size'):
                        data=self.request.recv(4096)
                        file_append.write(data)
                        recv_size+=len(data)
                    else:
                        file_append.close()
                        file_res=open(file_abs_path,'rb')
                        md5_3=hashlib.md5()
                        for i in file_res:
                            md5_3.update(i)
                        md5_val3=md5_3.hexdigest()
                        md5_dict={'md5':md5_val3}
                        self.send_head(md5_dict)
                    return True
                else:
                    res1_dict = {'ddfile_size': server_file_size,
                                'dd': False
                                }
                    print(res1_dict)
                    self.send_head(res1_dict)
            return False
        else:
            res1_dict = {'ddfile_size': 0,
                         'dd': False
                         }
            print('文件不存在：',res1_dict)
            self.send_head(res1_dict)
            return False







if __name__ == "__main__":
    HOST, PORT = "localhost", 9500
