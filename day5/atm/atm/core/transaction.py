#!_*_coding:utf-8_*_
#__author__:"Alex Li"

from conf import settings
from core import accounts
from core import logger
#transaction logger



def make_transaction(log_obj,account_data,tran_type,amount,**others):
    '''
    deal all the user transactions
    :param account_data: user account data
    :param tran_type: transaction type
    :param amount: transaction amount
    :param others: mainly for logging usage
    :return:
    '''
    amount = float(amount)
    if tran_type in  settings.TRANSACTION_TYPE: #判断传入type类型是否在配置文件中存在
        #interest：根据交易类型计算利息
        interest =  amount * settings.TRANSACTION_TYPE[tran_type]['interest']
        old_balance = account_data['balance']   #获取旧的余额
        if settings.TRANSACTION_TYPE[tran_type]['action'] == 'plus': #判断配置文件中，这种交易类型是进行什么操作：为加操作
            new_balance = old_balance + amount + interest               #新余额=旧余额+利息
        elif settings.TRANSACTION_TYPE[tran_type]['action'] == 'minus':#为减操作
            new_balance = old_balance - amount - interest   #新的余额=旧余额-利息
            #check credit
            if  new_balance <0: #如果操作完后的余额小于0
                print('''\033[31;1mYour credit [%s] is not enough for this transaction [-%s], your current balance is
                [%s]''' %(account_data['credit'],(amount + interest), old_balance ))    #打印你的余额不足以支付
                return  #返回退出
        account_data['balance'] = new_balance       #将用户信息中的余额修改为新的余额
        accounts.dump_account(account_data) #save the new balance back to file  #将用户数据保存到用户信息文件中
        log_obj.info("account:%s   action:%s    amount:%s   interest:%s" %
                          (account_data['id'], tran_type, amount,interest) )    #记录日志，交易日志
        return account_data #最后返回用户数据信息
    else:   #如果交易的类型不在配置文件中。打印这里
        print("\033[31;1mTransaction type [%s] is not exist!\033[0m" % tran_type)
