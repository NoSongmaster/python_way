# #liuhao
# '''
# 用于从文件里加载和储存账户数据
# '''
import os,sys,json
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
account_dir=BASE_DIR+"\\db\\accounts\\"
def account_get(account_id):    #获取账户信息
    if os.path.isfile(account_dir+str(account_id)):
        with open(account_dir+str(account_id),'r',encoding='utf-8') as f:
            account_data=json.loads(f.read())
        return account_data
    else: return False
def account_modify(account_id,key,value):   #修改账户信息
    account_data=account_get(account_id)
    if account_data == 'False':
        return False
    else:
        if key in account_data:
            account_data[key]=value
            with open(account_dir+str(account_id),'w',encoding='utf-8') as f:
                f.write(json.dumps(account_data))
            return True
        else:return False

if __name__ == '__main__':
    print(account_get(123))
    print(account_modify("123",'name','liuhao'))


