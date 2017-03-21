#liuhao
import shelve,os
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR+r"\users_database")
def auth_user(func):
    def auth(*args,**kwargs):         #用户验证函数
        status=0
        while status<3:
            flag = 0                                                #标记用户不存在，判断次数
            file=shelve.open(BASE_DIR+r"\users_database")                  #打开用户信息文件
            username=input("请输入你的用户名: ").strip()        #
            print(BASE_DIR)
            if len(username) == 0:                               #判断用户是否输入
                continue
            for key,name in enumerate(file):                    #判断用户是否存在
                # print(name)
                if name==username:
                    if file[username].get("status")>=3:         #判断用户是否锁定，锁定：退出。未锁定：输出可以尝试的次数
                        print("用户%s已锁定,请联系管理员解锁"%username)
                        exit()
                    else:
                        print("用户还有%s次机会尝试密码"%(3-file[username].get("status"))) #显示
                    password=input("请输入您的密码: ").strip()
                    # password = getpass.getpass(prompt="用户密码[空:退出]: ").strip()      #不显示输入的密码，在pycharm中不可使用~~
                    if len(password)==0:
                        print("密码不能为空")
                        continue

                    if password == file[username].get('password'):  #验证用户登录成功
                        print('''
                        ----用户 {username} 验证成功----

                             欢迎您的到来!!!
                        '''.format(username=username))
                        func(*args,**kwargs)
                        user_data = file[username]
                        user_data["status"] = 0                 #将用户信息中的锁定信息重置
                        file[username] = user_data               #重新保存到用户信息中
                        # print(file[username])
                        file.close()
                        exit()
                    else:
                        print("用户登录失败！！！")
                        user_data=file[username]
                        user_data["status"]+=1                  #将用户的失败次数+1
                        file[username]=user_data
                        if file[username].get("status")>=3:
                            print("用户已锁定")
                            file.close()
                            exit()
                else:
                    flag+=1                          #对file进行判断用户不存在，
                    if flag == len(file):              #对全部用户判断完成，全部不存在
                        print("用户不存在")         #输出：用户不存在
            file.close()    #循环完以后关闭文件
    return auth()
# @auth_user
# def p():
#     print(123444)
# p()
