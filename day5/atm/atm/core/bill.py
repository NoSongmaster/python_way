#liuhao
'''
账单记录模块
'''
import os,time
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def bill(account_id,type=None,money=0,msg=''):  #根据传入数据，记录用户操作账单
    log_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  #获取当前时间
    log_file = BASE_DIR + '\\db\\accounts\\' + str(account_id) + '.bill' #拼接用户账单文件
    with open(log_file,'a+',encoding='utf-8') as f:
        log_str=log_time.ljust(15,' ')+' 账户: '+str(account_id).ljust(10,' ')+' 操作类型 '+str(type.ljust(10,' '))+' 金额 '+str(money).ljust(10,' ')+ ' 消息 '+str(msg)+'\n'
        f.write(log_str)
def bill_get(account_id):   #获取账单时调用
    log_file = BASE_DIR + '\\db\\accounts\\' + str(account_id) + '.bill'
    with open(log_file,'r',encoding='utf-8')as f:
        a=f.read()
    return a



