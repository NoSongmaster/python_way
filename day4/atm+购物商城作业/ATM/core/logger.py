#liuhao
'''
日志记录模块
'''
import os,sys,time
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

def logger(account_id,type=None,money=0,msg=''):
    log_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    log_file = BASE_DIR + '\\log\\' + str(account_id) + '.log'
    with open(log_file,'a+',encoding='utf-8') as f:
        log_str=log_time.ljust(15,' ')+' 账户: '+str(account_id).ljust(10,' ')+' 操作类型 '+str(type.ljust(10,' '))+' 金额 '+str(money).ljust(10,' ')+ ' 消息 '+str(msg)+'\n'
        f.write(log_str)
def logger_get(account_id):
    log_file = BASE_DIR + '\\log\\' + str(account_id) + '.log'
    with open(log_file,'r',encoding='utf-8')as f:
        a=f.read()
    return a



