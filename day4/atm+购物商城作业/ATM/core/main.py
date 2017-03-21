#liuhao
'''
主逻辑交互程序
'''
import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core import transaction
from core.auth import *
@auth
def welcome():
    print('welcome to bank')
def run():
    account_id=welcome()
    dic={
        '1':transaction.withdrawals,
        '2':transaction.refund,
        '3':transaction.transfer,
        '4':transaction.query
    }
    while True:
        print('''
        1.  取现
        2.  还款
        3.  转账
        4.  查询
        退出【任意键】
        ''')
        choice=input(">>").strip()
        if choice in dic:
            dic[choice](account_id)
        else:
            return

if __name__ == '__main__':
    run()

