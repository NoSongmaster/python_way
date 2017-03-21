#liuhao
import shelve,getpass
def admin_user():         #用户管理函数
    choice=input('''
    用户管理：
    1、添加用户
    2、解锁用户
    3、查看所有用户
    【其它按键退出】
    ''')
    if choice=='1':
        while True:
            file = shelve.open("users_database")
            username = input("创建用户[空:退出]: ").strip()
            if len(username) == 0:
                print("用户名不能为空")
                break
            for key, name in enumerate(file):
                if username == name:
                    print("用户%s已经存在！！"%username)
                    exit()
            #password = input("用户密码[空:退出]: ").strip()
            password = getpass.getpass(prompt="用户密码[空:退出]: ").strip()     # 不显示输入的密码，在pycharm中不可使用~~
            if len(password) == 0:
                print("密码不能为空")
                break
            file[username]={"username":username,"password":password,"status":0}
            file.close()
            break
    elif choice=='2':
        flag=0
        file=shelve.open("users_database")
        username=input("输入要解锁的用户名：").strip()
        for key,name in enumerate(file):
            # print(key,name)
            if username ==name:
                user_data = file[username]
                user_data['status']=0
                file[username]=user_data
                file.close()
                print("解锁成功")
            else:
                flag+=1                          #对file进行判断用户不存在，
                if flag==len(file):              #对全部用户判断完成，全部不存在
                    print("用户不存在")         #输出：用户不存在
    elif choice=='3':
        file = shelve.open("users_database")
        for key,name in enumerate(file):
            print(name)

admin_user()