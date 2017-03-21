#liuhao
'''
用户认证模块
'''
import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
def auth(func):
    def wapper(*args,**kwargs):
        times=0
        while times <3:
            from core import accounts
            account_id=input("enter your account_id :")
            account_data=accounts.account_get(account_id)
            if account_data is False:

                print("您输入的account_id 不存在！")
                times+=1
                if times==3:return False
            else:
                if account_data['status'] ==3:
                    print("账号: %s 已锁定，请联系管理员解锁！"%account_id)
                    return False
                password=input("enter your password :")
                if password == account_data['password']:
                    accounts.account_modify(account_id,'status',0)
                    if func(*args,**kwargs) is False:return False
                    return account_id
                else:
                    times+=1
                    count=account_data['status']
                    count +=1
                    print("登录失败，还可以尝试 %s 次" % (3 - count))
                    accounts.account_modify(account_id,'status',count)
                    if count==3:
                        print("账号: %s 已锁定，请联系管理员解锁！"%account_id)
                        return False
    return wapper





if __name__ == '__main__':
    @auth
    def a():
        print("执行程序")
    a()