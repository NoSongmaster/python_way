#!_*_coding:utf-8_*_
#__author__:"Alex Li"

'''
main program handle module , handle all the user interaction stuff

'''

from core import auth
from core import accounts
from core import logger
from core import accounts
from core import transaction
from core.auth import login_required
from core import bill
import time

#transaction logger
trans_logger = logger.logger('transaction')
#access logger
access_logger = logger.logger('access')


#temp account data ,only saves the data in memory
user_data = {
    'account_id':None,
    'is_authenticated':None,
    'account_data':None
}
def show_some(acc_data):
    account_data = accounts.load_current_balance(acc_data['account_id'])#通过用户ID 加载获取用户数据
    current_balance= ''' --------- BALANCE INFO --------
        Credit :    %s
        Balance:    %s''' %(account_data['credit'],account_data['balance'])
    print(current_balance)  #打印用户额度和余额
    return account_data

def account_info(acc_data):
    account_data = accounts.load_current_balance(acc_data['account_id'])
    while True:
        print('''
            -----------账户信息----------\033[32;1m
            id:{id}
            credit: {credit}
            balance: {balance}
            enroll_date: {enroll_date}
            expire_date: {expire_date}
            pay_day: {pay_day}
            status: {status}
        \033[0m'''.format(id=account_data['id'],credit=account_data['credit'],balance=account_data['balance'],enroll_date=account_data['enroll_date'],
                   expire_date=account_data['expire_date'],pay_day=account_data['pay_day'],status=account_data['status']))
        choice=input(">>:")
        if choice =='b':return

@login_required
def repay(acc_data):    #进行还款操作
    '''
    print current balance and let user repay the bill
    :return:
    '''
    account_data = show_some(acc_data)
    back_flag = False
    while not back_flag:
        repay_amount = input("\033[33;1mInput repay amount:\033[0m").strip()    #传入还款的金额
        if len(repay_amount) >0 and repay_amount.isdigit(): #如果传入的还款金额是整数并且不为空
            account_newdata = transaction.make_transaction(trans_logger,account_data,'repay', repay_amount)  #这里获取到的是新的用户信息
            if account_newdata: #如果获取到的新用户信息为真
                print('''\033[42;1mNew Balance:%s\033[0m''' %(account_newdata['balance']))  #打印新的余额
                bill.bill(account_data['id'],type='repay',money='+'+str(repay_amount),msg="action from atm")
        elif repay_amount == 'b': #如果输入的是b，将循环条件设置为真，跳出循环
            back_flag = True
        else:   #传入的不是整数或者为空，输出下面的值
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % repay_amount)



def withdraw(acc_data):
    '''
    print current balance and let user do the withdraw action
    :param acc_data:
    :return:
    '''
    account_data = show_some(acc_data)#打印用户额度和余额

    back_flag = False   #循环标签
    while not back_flag:    #
        withdraw_amount = input("\033[33;1mInput withdraw amount:\033[0m").strip()  #用户输入取现的金额
        if len(withdraw_amount) >0 and withdraw_amount.isdigit():   #判断用户输入的是整数并且不为空
            account_newdata = transaction.make_transaction(trans_logger,account_data,'withdraw', withdraw_amount)#通过计算得到新的用户信息data
            if account_newdata: #如果获取到了新的用户信息
                print('''\033[42;1mNew Balance:%s\033[0m''' %(account_newdata['balance']))  #打印新的余额
                bill.bill(account_data['id'], type='withdraw', money='-' + str(withdraw_amount), msg="action from atm")
        elif withdraw_amount == 'b':#如果用户输入b 修改循环条件，跳出循环
            back_flag = True
        else:   #如果用户输入的不是整数或者为空
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % withdraw_amount)



def transfer(acc_data): #转账功能
    account_data=show_some(acc_data)
    back_flag = False   #循环标签
    while not back_flag:    #
        transfer_amount =input("\033[33;1mInput transfer amount:\033[0m").strip()           #输入要转账的金额
        if len(transfer_amount) > 0 and transfer_amount.isdigit():
            transfer_id=input("\033[33;1mInput transfer id:\033[0m").strip()                #输入要转入的账户
            if len(transfer_id) > 0 and transfer_id.isdigit():
                if transfer_id==account_data['id']:                                               #判断用户是否给自己转账
                    print("\033[31;1m不能给自己转账\033[0m")
                    continue
                transfer_account_data=accounts.load_current_balance(transfer_id)        #加载对方的数据
                if transfer_account_data :                                              #对方账户存在
                    account_newdata = transaction.make_transaction(trans_logger, account_data, 'transfer', transfer_amount) #将自己账户进行减金额操作
                    if account_newdata: #确定自己账户减操作完成
                        bill.bill(account_data['id'], type='transfer', money='-' + str(transfer_amount),msg="action from atm, transfer to %s" % transfer_id)  # 记录账单
                        transaction_new_data=transaction.make_transaction(trans_logger,transfer_account_data,'repay',transfer_amount)   #对方账户进行加金额操作
                        bill.bill(transfer_id, type='transfer', money='+' + str(transfer_amount),msg="action from atm, transfer from %s" %account_data['id'])#为对方记录账单
                        if transaction_new_data:    #确认操作完成
                            print("\033[42;1m转账成功\033[0m")
            elif transfer_id =='b':return
            else:print("\033[31;1m未成功-请重试\033[0m")
        elif transfer_amount =='b': return

def pay_check(acc_data):    #打印账单
    back_flag = False
    while not back_flag:
        print(bill.bill_get(acc_data['account_id']))#根据用户id打印该用户的账单
        choice=input(">>:")
        if choice=='b':
            back_flag=True
def logout(acc_data):
    exit("程序退出！欢迎下次光临")
@login_required #验证是否已经认证密码
def payment_api(acc_data,money='0',msg=''): #购物车调用的api接口
    account_data=show_some(acc_data)         #获取用户数据
    if account_data:
        if int(money) > 0 and money.isdigit():  #判断传入的参数
            account_newdata = transaction.make_transaction(trans_logger, account_data, 'consume', money)    #用户数据进行减金额操作
            if account_newdata:
                bill.bill(account_data['id'], type='consume', money='-' + str(money), msg="action from shopping"+str(msg))  #记录账单
            return True
        else:return False
    else:return False
def interactive(acc_data):
    '''
    interact with user
    :return:
    '''
    menu = u'''
    ------- Oldboy Bank ---------\033[32;1m
    1.  账户信息(功能已实现)
    2.  还款(功能已实现)
    3.  取款(功能已实现)
    4.  转账(功能已实现)
    5.  账单(功能已实现)
    6.  退出(功能已实现)
    \033[0m'''
    menu_dic = {
        '1': account_info,
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': pay_check,
        '6': logout,
    }
    exit_flag = False
    while not exit_flag:    #进入循环
        print(menu)         #打印菜单
        user_option = input(">>:").strip()  #等待用户输入选项
        if user_option in menu_dic:     #如果输入的选项在字典里
            menu_dic[user_option](acc_data) #执行选项下的函数

        else:
            print("\033[31;1mOption does not exist!\033[0m")
def run():
    '''
    this function will be called right a way when the program started, here handles the user interaction stuff
    :return:
    '''
    #返回用户数据acc_data.
    acc_data = auth.acc_login(user_data,access_logger)  #获取到了用户数据
    if user_data['is_authenticated']:#如果验证通过
        user_data['account_data'] = acc_data    #将用户数据存到user_data['account_data']中。
        interactive(user_data)                     #调用银行功能