#!_*_coding:utf-8_*_
#__author__:"Alex Li"

'''
handle all the database interactions
'''
import json,time ,os
from  conf import settings
def file_db_handle(conn_params):
    '''
    parse the db file path
    :param conn_params: the db connection params set in settings
    :return:
    '''
    #print('file db:',conn_params)
    #db_path ='%s/%s' %(conn_params['path'],conn_params['name'])
    return file_execute

def db_handler():
    '''
    connect to db
    :param conn_parms: the db connection params set in settings
    :return:a
    '''
    conn_params = settings.DATABASE #读取conf下的setting配置文件。
    if conn_params['engine'] == 'file_storage': #判断配置文件中，用户信息读取方式。这里是文件存储
        return  file_execute    #此处已修改，返回文件存储，数据操作函数file_execute的内存地址
        #return file_db_handle(conn_params)
    elif conn_params['engine'] == 'mysql':  #如果从配置文件中读取到的是mysql存储，执行这里
        pass #todo



def file_execute(sql,**kwargs):
    conn_params = settings.DATABASE     #读取配置文件中的DATABASE
    db_path = '%s/%s' % (conn_params['path'], conn_params['name'])  #读取db_path路径

    sql_list = sql.split("where")   #切割传入的sql 语句
    if sql_list[0].startswith("select") and len(sql_list)> 1:#has where clause  #如果是slect 语句，读取用户信息
        column,val = sql_list[1].strip().split("=") #对where后面的语句进行切割。获取到accout字段和用户名

        if column == 'account':     #如果获取的字段为account
            account_file = "%s/%s.json" % (db_path, val)    #用户文件路径进行拼接
           # print(account_file)
            if os.path.isfile(account_file):    #判断拼接得到的account_file是一个文件
                with open(account_file, 'r') as f:  #读取用户信息文件
                    account_data = json.load(f)
                    return account_data #返回用户信息
            else:
                return False
                #exit("\033[31;1mAccount [%s] does not exist!\033[0m" % val )    #其它的退出打印，用户不存在

    elif sql_list[0].startswith("update") and len(sql_list)> 1:#has where clause    #如果是要更新用户数据，判断update
        column, val = sql_list[1].strip().split("=")    #对传入的sql语句进行切割
        if column == 'account': #判断account字段
            account_file = "%s/%s.json" % (db_path, val)    #拼接用户文件
            #print(account_file)
            #if os.path.isfile(account_file):    #判断用户文件是否存在
            account_data = kwargs.get("account_data")   #这里会传入user_data 读取user_data['account_data']是用户信息
            with open(account_file, 'w') as f:
                acc_data = json.dump(account_data, f)       #将用户信息重新写入到用户数据文件中，
            return True                             #返回True