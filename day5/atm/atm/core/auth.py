#!_*_coding:utf-8_*_
#__author__:"Alex Li"
import os,sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from core import db_handler
from conf import settings
from core import logger
from core import accounts
import json
import time
access_logger = logger.logger('access')


def login_required(func):
    "验证用户是否登录"

    def wrapper(*args,**kwargs):
        #print('--wrapper--->',args,kwargs)
        if args[0].get('is_authenticated'):
            return func(*args,**kwargs)
        else:
            exit("User is not authenticated.")
    return wrapper


def acc_auth(account,password):
    '''
    account auth func
    :param account: credit account number
    :param password: credit card password
    :return: if passed the authentication , retun the account object, otherwise ,return None
    '''
    db_path = db_handler.db_handler(settings.DATABASE)
    account_file = "%s/%s.json" %(db_path,account)
    print(account_file)
    if os.path.isfile(account_file):
        with open(account_file,'r') as f:
            account_data = json.load(f)
            if account_data['password'] == password:
                exp_time_stamp = time.mktime(time.strptime(account_data['expire_date'], "%Y-%m-%d"))
                if time.time() >exp_time_stamp:
                    print("\033[31;1mAccount [%s] has expired,please contact the back to get a new card!\033[0m" % account)
                else: #passed the authentication
                    return  account_data
            else:
                print("\033[31;1mAccount ID or password is incorrect!\033[0m")
    else:
        print("\033[31;1mAccount [%s] does not exist!\033[0m" % account)


def acc_auth2(account,password):
    '''
    优化版认证接口
    :param account: credit account number
    :param password: credit card password
    :return: if passed the authentication , retun the account object, otherwise ,return None

    '''
    db_api = db_handler.db_handler()    #调用dbhandle.db_handler()。这里返回的是file_execute
    data = db_api("select * from accounts where account=%s" % account)  #调用file_execute(传入sql)
    if data is False:return
    if data['password'] == password:        #验证用户输入的密码
        exp_time_stamp = time.mktime(time.strptime(data['expire_date'], "%Y-%m-%d"))    #验证本地时间和信用卡过去时间
        if time.time() > exp_time_stamp:#判断信用卡是否过期
            print("\033[31;1mAccount [%s] has expired,please contact the back to get a new card!\033[0m" % account)#打印过期信息
        else:  # passed the authentication
            return data #返回获取到的用户数据
    else:
        print("\033[31;1mAccount ID or password is incorrect!\033[0m")  #打印用户名或密码错误

def acc_login(user_data,log_obj):
    '''
    account login func
    :user_data: user info data , only saves in memory
    :return:
    '''
    retry_count = 0
    while user_data['is_authenticated'] is not True and retry_count < 3 :   #判断user_data['is_authenticated']是否已经通过验证，并判断用户尝试次数
        account = input("\033[32;1maccount:\033[0m").strip()
        '''缺少判断账户是否已经锁定'''
        account_data=accounts.load_current_balance(account)
        if account_data is False:
            print("\033[31;1m用户%s不存在\033[0m"%account)
            continue
        elif account_data['status']>=3:
            print("\033[31;1m用户%s已经锁定，请联系管理员！\033[0m"%account)
            return
        times = account_data['status']
        while retry_count<3:
            password = input("\033[32;1mpassword:\033[0m").strip()
            auth = acc_auth2(account, password)                         #调用acc_auth2验证用户输入的用户名和密码，返回用户数据data
            if auth: #not None means passed the authentication      #如果auth获取到了字典
                user_data['is_authenticated'] = True    #将user_data改成已经完成验证
                user_data['account_id'] = account           #将account_data存入user_data。省去查询时候调用
                account_data['status']=0                     #登录成功后，重置status
                accounts.dump_account(account_data)
                return auth                                 #返回account_data 用户信息
            times +=1                                 #用户尝试次数
            '''缺少锁定账户'''
            account_data['status'] = times
            accounts.dump_account(account_data)
            if times == 3:
                log_obj.error("account [%s] too many login attempts" % account)
                return
            retry_count += 1
            if retry_count == 3:
                log_obj.error("account [%s] too many login attempts" % account)  # logger记录登录失败信息

    else:   #登录三次失败以后。

        log_obj.error("account [%s] too many login attempts, is locked " % account) #logger记录登录用户已经锁定信息
        exit()

def auth_api(func):#  装饰器认证用户信息     用于购物车程序
    def wapper(*args,**kwargs):
        user_data = {
            'account_id': None,
            'is_authenticated': None,
            'account_data': None
        }
        acc_data=acc_login(user_data,access_logger)
        if user_data['is_authenticated']:  # 如果验证通过
            user_data['account_data'] = acc_data  # 将用户数据存到user_data['account_data']中。
        return user_data
    return wapper
