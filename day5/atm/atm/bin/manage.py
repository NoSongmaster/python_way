'''
创建atm账户，解锁账户
'''
import sys,os,datetime,time

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from db import account_sample
from core import accounts
def account_create():   #创建账户模块

    account_id = input("create your account_id :").strip()  #用户输入要创建的用户account_id
    if len(account_id)>0 and account_id.isdigit():    #如果输入的值不为空并且是整数
        if accounts.load_current_balance(account_id):   #加载用户数据
            print("账号已存在")
            return
        for i in account_sample.acc_dic:    #   #循环初始化用户数据信息
            if i =='id':    #如果循环到id使用，用户输入的account_id
                new_data=int(account_id)
            elif i in ['credit','balance','status','pay_day']:  #如果在这里的
                new_data=account_sample.acc_dic[i]
            elif i =='enroll_date':
                #new_data=datetime.datetime.now()
                new_data=time.strftime("%Y-%m-%d")      #记录当前日期为信用卡注册时间
            elif i =='expire_date':
                struct_time = time.localtime(time.time() + 10 * 365 * 86400)
                new_data=time.strftime("%Y-%m-%d", struct_time) #记录卡失效时间为10年
            elif i =='password':
                new_data=input("enter your password:")   #用户输入password
            account_sample.acc_dic[i]=new_data  #每次循环完成为account_dic赋新值
        print(account_sample.acc_dic)
        accounts.dump_account(account_sample.acc_dic)   #将用户文件存储到本地
    else:return

def account_unlock():   #解锁用户信息

    account_id=input("Enter the account_id you want to unlock :")   #输入要解锁的id
    account_data=accounts.load_current_balance(account_id)      #加载用户信息
    if account_data is False:       #如果返回的信息是False
        print("账号不存在")
        return
    if len(account_id) == 0: return #如果输入的密码为空，直接返回
    account_data['status']=0        #将加载到的用户信息status设置为0
    flag=accounts.dump_account(account_data)    #保存用户信息到本地
    if flag:    #查看保存信息的返回值
        print('解锁成功')
    else:print("解锁未成功")

if __name__ == '__main__':
    while True:
        menu={'1':account_create,'2':account_unlock}
        print('''
        1、创建账号
        2、解锁账号
        ''')
        choice=(input('请输入>>[q]').strip())
        if choice == 'q':exit()
        elif choice in menu:
            menu[choice]()
        else:
            print('输入有误')