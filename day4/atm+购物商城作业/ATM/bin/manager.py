#liuhao
'''ATM 管理端'''
'''
创建atm账户，解锁账户
'''
import sys,os

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core import accounts
from db import account_sample
def account_create():

    account_id = input("create your account_id :").strip()
    if len(account_id)==0:return
    if accounts.account_get(account_id) is not False:
        print("账号已存在")
        return
    name=input("enter your name :").strip()
    if len(name) == 0: return
    password=input("enter your password :").strip()
    if len(password) == 0: return
    account_sample.make_account(account_id,name,password)
def account_unlock():

    account_id=input("Enter the account_id you want to unlock :")
    if accounts.account_get(account_id) is False:
        print("账号不存在")
        return
    if len(account_id) == 0: return
    flag=accounts.account_modify(account_id,'status',0)
    if flag:
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


