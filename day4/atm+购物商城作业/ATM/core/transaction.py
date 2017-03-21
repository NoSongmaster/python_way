#liuhao
'''
记账\还钱\取钱等所有的与账户金额相关的操作都在这里
'''
import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core import accounts
from core import logger     #logger(account_id,type=None,money=0,msg='')
from core import auth
#判断函数
def judge(account_id,money):
    account_data=accounts.account_get(account_id)
    if account_data['money']<money:
        print("账户：%s 余额不足,剩余金额: %s"%(account_id,account_data['money']))
        return False
    else:
        return True
#计算函数
def compute(account_id,type=None,money=0,account_id2=None):
    dic={1:withdrawals,2:refund,3:transfer,4:payment_api}
    if type in dic:
        if type == 1:
            account_data1=accounts.account_get(account_id)
            money=account_data1['money']-money*1.05 #利息为5%
            accounts.account_modify(account_id,'money',money)
        elif type == 2:
            account_data1=accounts.account_get(account_id)
            money=account_data1['money']+money
            accounts.account_modify(account_id,'money',money)
        elif type == 3:
            account_data1=accounts.account_get(account_id)
            money1=account_data1['money']-money
            accounts.account_modify(account_id,'money',money1)
            account_data2=accounts.account_get(account_id2)
            money2=account_data2['money']+ money
            accounts.account_modify(account_id2,'money',money2)
        elif type == 4:
            account_data=accounts.account_get(account_id)
            money=account_data['money']-money
            accounts.account_modify(account_id,'money',money)
#提现
def withdrawals(account_id):
    money=input("请输入要提现的金额[ 5% ][b]: ").strip()
    if money == 'b':return
    elif money.isdigit():
        money=int(money)
    else:
        print("输入有误")
        return
    bo=judge(account_id,money)
    if bo:
        compute(account_id,1,money)
        logger.logger(account_id,'提现','-'+str(money))
    else:return False
#还款
def refund(account_id):
    money = input("请输入要还款的金额[b]: ").strip()
    if money == 'b':return
    elif money.isdigit():
        money=int(money)
    else:
        print("输入有误")
        return
    compute(account_id,2,money)
    logger.logger(account_id, '还款', '+' + str(money))
    return False
#转账
def transfer(account_id):
    money = input("请输入要转账的金额[b]: ").strip()
    if money == 'b':return
    elif money.isdigit():
        money=int(money)
    else:
        print("输入有误")
        return
    account_id2=input("请输入转入的账户[b]:").strip()
    if account_id2=='b':return
    elif account_id2.isdigit():
        if account_id2==account_id:
            print("不能给本账户转账")
            return
        elif accounts.account_get(account_id2) is False:
            print(" 账户: %s 不存在"%account_id2)
            return
        else:account_id2=int(account_id2)
        bo=judge(account_id,money)
        if bo:
            compute(account_id,3,money,account_id2)
            logger.logger(account_id, '转出', '-' + str(money),msg='转入账户%s'%account_id2)
            logger.logger(account_id2,'转入','+'+str(money),msg='来自%s的转账'%account_id)
        else:return  False
    else:print("输入有误")

#查询
def query(account_id):
    account_data=accounts.account_get(account_id)
    choice=input('''
        账户 ID: %s        额度: %s
        1、 查询账户余额
        2、 查询账单
        [任意键退出]
    '''%(account_id,account_data['quota']))
    if choice=='1':
        print('\t\t额度为:%s\t可用金额为:%s'%(account_data['quota'],account_data['money']))
    if choice=='2':
        print(logger.logger_get(account_id))
    else:return

def payment_api(account_id=0,money=0,msg=''):
    bo = judge(account_id, money)
    if bo:
        compute(account_id,4,money)
        logger.logger(account_id,'购物','-'+ str(money),msg)
        return True
    else:return False

if __name__ == '__main__':
    payment_api(123,10000)
